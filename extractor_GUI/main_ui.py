from extractor_ui import Ui_mainWindow
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import threading
from extractor_script.extractor import extract




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
        self.depth = self.ui.depth.value()


        sys.stdout = Stream(newText=self.onUpdateText)

    def onUpdateText(self, text):
        cursor = self.ui.extracted_emails.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.extracted_emails.setTextCursor(cursor)
        self.ui.extracted_emails.ensureCursorVisible()

    def __del__(self):
        sys.stdout = sys.__stdout__


    
    # def gg(self):
    #     for n in range(5):
    #         time.sleep(1)
    #         print("processing" + str(n))

    def link_extract(self):
        print(self.depth)

        t1 = threading.Thread(target=self.gg)
        t1.start()
        
        

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