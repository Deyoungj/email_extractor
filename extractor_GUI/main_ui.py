from extractor_ui import Ui_mainWindow
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from qt_thread_updater import get_updater
import time
import threading
from extractor_script import extract
import requests, re
from bs4 import BeautifulSoup
from collections import deque
import urllib


class CustomThread(threading.Thread):
    def __init__(self,group=None, target=None,name=None, args=(), kwargs={}, verbose=None):
        threading.Thread.__init__(self,group, target, name, args, kwargs)

        self._return_value = None

    def run(self):
        if self._target is not None:

            self._return_value = self._target(*self._args, **self._kwargs)

            return self._return_value



class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class Ui_Window(QtWidgets.QMainWindow):
    
    def __init__(self) -> None:
        super(Ui_Window, self).__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.kill = False

        self.mail_type = {
            "All": r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z\.]+",
            "gmail": r"[a-zA-Z0-9\.\-+_]+@gmail+\.[a-z\.]+",
            "hotmail": r"[a-zA-Z0-9\.\-+_]+@hotmail+\.[a-z\.]+",
            "sbcglobal": r"[a-zA-Z0-9\.\-+_]+@sbcglobal+\.[a-z\.]+",
            "yahoo": r"[a-zA-Z0-9\.\-+_]+@yahoo+\.[a-z\.]+",
            "outlook": r"[a-zA-Z0-9\.\-+_]+@outlook+\.[a-z\.]+",
            "live": r"[a-zA-Z0-9\.\-+_]+@live+\.[a-z\.]+",
            "att": r"[a-zA-Z0-9\.\-+_]+@att+\.[a-z\.]+",
            "rocketmail": r"[a-zA-Z0-9\.\-+_]+@rocketmail+\.[a-z\.]+",
            "aol": r"[a-zA-Z0-9\.\-+_]+@aol+\.[a-z\.]+",
            "wanadoo": r"[a-zA-Z0-9\.\-+_]+@wanadoo+\.[a-z\.]+",
            "orange": r"[a-zA-Z0-9\.\-+_]+@orange+\.[a-z\.]+",
            "rediffmail": r"[a-zA-Z0-9\.\-+_]+@rediffmail+\.[a-z\.]+",
            "free": r"[a-zA-Z0-9\.\-+_]+@free+\.[a-z\.]+",
            "gmx": r"[a-zA-Z0-9\.\-+_]+@gmx+\.[a-z\.]+",
            "blueyonder": r"[a-zA-Z0-9\.\-+_]+@blueyonder+\.[a-z\.]+",
            "skynet": r"[a-zA-Z0-9\.\-+_]+@skynet+\.[a-z\.]+",
            "comcast": r"[a-zA-Z0-9\.\-+_]+@comcast+\.[a-z\.]+",
            "bellsouth": r"[a-zA-Z0-9\.\-+_]+@bellsouth+\.[a-z\.]+",
            "laposte": r"[a-zA-Z0-9\.\-+_]+@laposte+\.[a-z\.]+",
        }

        self.home = os.path.expanduser('~')
        self.filter = "txt(*.txt)"

        # buttons in the link extract tab
        self.ui.link_cancel_btn.setEnabled(False)
        if self.ui.text_email_extract.toPlainText() == "":
            self.ui.text_save_btn.setEnabled(False)

        self.ui.link_extract_btn.clicked.connect(self.link_extract)
        self.ui.link_cancel_btn.clicked.connect(self.link_cancel)
        self.ui.save_to_file_btn.clicked.connect(self.link_save)
        
        
        # buttons in the text extract tab
        self.ui.text_extract_btn.clicked.connect(self.text_extract)
        self.ui.text_save_btn.clicked.connect(self.text_save)

        
        # depth of the link
        
        self.output = self.ui.process_output

        sys.stdout = Stream(newText=self.onUpdateText)


        self.emails_extracted_list =""""""



    def onUpdateText(self, text):
        cursor = self.output.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.output.setTextCursor(cursor)
        self.output.ensureCursorVisible()


    def __del__(self):
        sys.stdout = sys.__stdout__



    def process_link(self, url: str , length: int, email_regx = '') -> list:
        
        unprocessed_links = deque([url])

        processed_url = []
        emails  = set()

        count = 0

        
        while unprocessed_links:
            count += 1
            if count == length:
                break

            if self.kill:
                break

            url = unprocessed_links.popleft()
            processed_url.append(url)
            # print("urls: %s" %url)

            parts = urllib.parse.urlsplit(url)
            base = f"{parts.scheme}://{parts.netloc}"
            path = url[:url.rfind("/")+1] if "/" in parts.path else url
            # print(path)
            
            if url.startswith("https://"):
                url = url
            else:
                url = "https://"+url

            try:
                response = requests.get(url, timeout=10)
                    
            except(requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
                self.ui.extracting.setStyleSheet("color: rgb(224, 27, 36);")
                self.ui.extracting.setText("connection error")
            

                
            if response.status_code != 200:
                self.ui.process_output.setStyle("color: rgb(224, 27, 36);")
                print(f"--------[{count}]**  processing link: [{url}] **status: [{response.status_code}] \n")
                self.ui.process_output.setStyle("color: rgb(0, 0, 0));")

            else:
                self.ui.process_output.setStyle("color: rgb(0, 0, 0));")
                print(f"--------[{count}]**  processing link: [{url}] **status: [{response.status_code}] \n")


            new_email = re.findall(email_regx, response.text, re.I)
            emails.update(new_email)
            # print(new_email)

            soup = BeautifulSoup(response.text, "html.parser")


            for anchor in soup.find_all("a"):
                link =  anchor.attrs["href"] if "href" in anchor.attrs else ""
                if link.startswith("/"):
                    link = base + link
                if not link.startswith("http"):
                    link = path + link
                if not link in unprocessed_links or not link in processed_url:
                    if "youtube" in link or "payments" in link or "myaccount.google.com" in link or "support.google.com" in link or "policies" in link or "play.google.com" in link or "map.google.com" in link or "mail.google.com" in link or "news.google.com" in link or "drive.google.com" in link or "history" in link or "advanced_search" in link or "preferences" in link:
                        pass
                    else:
                        unprocessed_links.append(link)

        for mail in emails:
            get_updater().call_in_main(self.ui.extracted_emails.append, mail)
            time.sleep(0.01)
                    

        return emails



    def extract(self, urls: list, length: int = 5, email_regx = '') -> set:

        # print(urls)

        # queue of urls to be crawled
        unprocessed_urls = deque(urls)

        # set of already crawled urls for email
        processed_urls = []

        # all emails goten from the links
        all_emails = set()
        count = 0

        while unprocessed_urls:

            if self.kill:
                break

            url = unprocessed_urls.popleft()
            processed_urls.append(url)


            print(" processing url: %s" % url + "\n \n")
            # self.ui.process_output.setText(" processing url: %s" % url + "\n \n")
            count += 1
            mails = self.process_link(url, length, email_regx)

            for mail in mails:
                all_emails.add(mail)


        # for mail in mails :
        #     with open("mails.txt", "a") as f:
        #         f.write(mail+"\n")
        
        # print("all emails has been saved ")
        
        
        for mail in all_emails:
            # self.ui.extracted_emails.append(mail)
            self.emails_extracted_list += mail+' \n'
        
        
        self.ui.extracting.setStyleSheet("color: rgb(87, 227, 137);")
        self.ui.extracting.setText("completed")

        
    def link_extract(self):
       
        # text = self.ui.link_input.text()
        if  self.ui.link_input.text() == '':
            self.ui.extracting.setStyleSheet("color: rgb(224, 27, 36);")
            self.ui.extracting.setText("no url found")
            
        else:
            
            self.ui.link_cancel_btn.setEnabled(True)
            self.ui.link_extract_btn.setEnabled(False)
            depth = self.ui.depth.value()
            email_type = self.ui.mail_type.currentText()
            mail_regx = self.mail_type[email_type]

            self.ui.process_output.clear()
            self.ui.extracted_emails.clear() 
            urls = str(self.ui.link_input.text()).split(',')

            self.ui.extracting.setStyleSheet("color: rgb(87, 227, 137);")
            self.ui.extracting.setText("Extracting ...")
            # print("hello")

            # print(self.ui.link_input.text())
            # print("hello")
            
            alive = threading.Event()
            thread = CustomThread(target=self.extract, args=(urls, depth, mail_regx) )
            thread.start()
            
    def text_extract_mails(self):
        text = self.ui.Text_to_extract.toPlainText()
        self.ui.text_email_extract.setText(text)

        new_email = re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", text, re.I)
        for mail in new_email:
            self.ui.text_email_extract.append(mail)


    def link_cancel(self):
        self.ui.link_cancel_btn.setEnabled(False)
        self.ui.link_extract_btn.setEnabled(True)
        self.kill = True


    def link_save(self):
        email = self.ui.extracted_emails.toPlainText()


        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', self.home, self.filter)
        file_path = ''

        if name[0].endswith('.txt') :
            file_path = name[0]

        else:
            file_path = name[0]+".txt"

        with open(file_path, "w") as f:
            f.write(email)
        

    def text_extract(self):
        self.text_extract_mails()
        self.ui.text_save_btn.setEnabled(True)

    def text_save(self):
        email = self.ui.text_email_extract.toPlainText()
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', self.home, self.filter)
        file_path = ''

        if name[0].endswith('.txt') :
            file_path = name[0]

        else:
            file_path = name[0]+".txt"

        with open(file_path, "w") as f:
            f.write(email)

    





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Window()
    window.show()
    sys.exit(app.exec_())