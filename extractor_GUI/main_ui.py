from extractor_ui import Ui_mainWindow
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import concurrent.futures
from threading import Thread
from extractor_script import extract
import requests, re
from bs4 import BeautifulSoup
from collections import deque
import urllib


class CustomThread(Thread):
    def __init__(self,group=None, target=None,name=None, args=(), kwargs={}, verbose=None):
        Thread.__init__(self,group, target, name, args, kwargs)

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

        

        # buttons in the link extract tab
        self.ui.link_cancel_btn.setEnabled(False)
        if self.ui.extracted_emails.toPlainText() == "":
            self.ui.save_to_file_btn.setEnabled(False)

        self.ui.link_extract_btn.clicked.connect(self.link_extract)
        self.ui.link_cancel_btn.clicked.connect(self.link_cancel)
        self.ui.save_to_file_btn.clicked.connect(self.link_save)
        self.ui.path_to_save_btn.clicked.connect(self.save_path)
        
        
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

    def process_link(self, url: str , length: int) -> list:
        
        unprocessed_links = deque([url])

        processed_url = []
        emails  = set()

        count = 0

        
        while unprocessed_links:
            count += 1
            if count == length:
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

            
            print(f"--------[{count}]**  processing link: [{url}] **status: [{response.status_code}] \n")


            new_email = re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
            emails.update(new_email)

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
                    

        return emails



    def extract(self, urls: list, length: int = 5) -> set:

        # print(urls)

        # queue of urls to be crawled
        unprocessed_urls = deque(urls)

        # set of already crawled urls for email
        processed_urls = []

        # all emails goten from the links
        all_emails = set()
        count = 0

        while unprocessed_urls:

            url = unprocessed_urls.popleft()
            processed_urls.append(url)

            print(" processing url: %s" % url + "\n \n")
            # self.ui.process_output.setText(" processing url: %s" % url + "\n \n")
            count += 1
            mails = self.process_link(url, length)

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
        # cursor = self.ui.process_output.textCursor()
        # cursor.movePosition(QtGui.QTextCursor.End)

        # text = self.ui.link_input.text()
        if  self.ui.link_input.text() == '':
            self.ui.extracting.setStyleSheet("color: rgb(224, 27, 36);")
            self.ui.extracting.setText("no url found")
            

        else:

            print(self.ui.link_input.text())
            

            depth = self.ui.depth.value()

            self.ui.process_output.clear() 
            urls = str(self.ui.link_input.text()).split(',')

            self.ui.extracting.setStyleSheet("color: rgb(87, 227, 137);")
            self.ui.extracting.setText("Extracting ...")
            # print("hello")

            # print(self.ui.link_input.text())
            # print("hello")
            

            thread = CustomThread(target=self.extract, args=(urls, depth) )
            thread.start()
            print(thread._return_value)

            
            
            

            # link = str(self.ui.link_input.text()).split(',')
            # print(link)




    def link_cancel(self):
        pass

    def save_path(self):
        pass

    def link_save(self):
            pass

    def text_extract(self):
        pass

    def text_save(self):
        pass

    





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Window()
    window.show()
    sys.exit(app.exec_())