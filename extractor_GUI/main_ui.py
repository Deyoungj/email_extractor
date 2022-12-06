from extractor_ui import Ui_mainWindow
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import threading
import time
import requests, re
from bs4 import BeautifulSoup
from collections import deque
import urllib



class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class Ui_Window(QtWidgets.QMainWindow):
    
    def __init__(self) -> None:
        super(Ui_Window, self).__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        sys.stdout = Stream(newText=self.onUpdateText)

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
        self.depth = self.ui.depth.value()


    def onUpdateText(self, text):
        cursor = self.ui.extracted_emails.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.extracted_emails.setTextCursor(cursor)
        self.ui.extracted_emails.ensureCursorVisible()

    def __del__(self):
        sys.stdout = sys.__stdout__


    def process_link(self, url: str , length: int ) -> list:
        
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
            print(path)
            
            if url.startswith("https://"):
                url = url
            else:
                url = "https://"+url

            try:
                response = requests.get(url, timeout=10)
            except:
                pass

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
                    if "youtube" in link or "payments" in link or "myaccount.google.com" in link or "support.google.com" in link or "policies" in link or "payments" in link:
                        pass
                    else:
                        unprocessed_links.append(link)
                    

        return emails


    def extract(self, url: list, length: int = 5):

        
        # all = "all"
        # hotmail = "hotmail"
        # gmail = "gmail"
        # outlook = "outlook"

        # queue of urls to be crawled
        unprocessed_urls = deque(url)

        # set of already crawled urls for email
        processed_urls = []

        # all emails goten from the links
        all_emails = set()
        count = 0

        while unprocessed_urls:

            url = unprocessed_urls.popleft()
            processed_urls.append(url)

            print(" processing url: %s" % url + "\n \n")
            count += 1
            mails = self.process_link(url, length)

            for mail in mails:
                all_emails.add(mail)


        # for mail in mails :
        #     with open("mails.txt", "a") as f:
        #         f.write(mail+"\n")
        
        # print("all emails has been saved ")
    def gg(self):
        for n in range(5):
            time.sleep(1)
            print("processing" + str(n))

    def link_extract(self):
        print(self.depth)

        t1 = threading.Thread(target=self.gg)
        t1.start()
        
        # self.gg()
        # print("hello")

        link = str(self.ui.link_input.text()).split(',')
        print(link)




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