# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extractor.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(910, 644)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono Medium for Powerline")
        mainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-mail-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono Medium for Powerline")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setStyleSheet("font: 57 11pt \"Roboto Mono Medium for Powerline\";")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.email_tab = QtWidgets.QWidget()
        self.email_tab.setObjectName("email_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.email_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.email_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 0)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.link_input = QtWidgets.QLineEdit(self.frame_8)
        self.link_input.setMaxLength(999999999)
        self.link_input.setObjectName("link_input")
        self.horizontalLayout.addWidget(self.link_input)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_12)
        self.label_5.setStyleSheet("\n"
"color: rgb(229, 165, 10);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setStyleSheet("color: rgb(245, 194, 17);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_12)
        self.label_7.setStyleSheet("color: rgb(245, 194, 17);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.horizontalLayout_4.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame_13)
        self.label_3.setStyleSheet("font: 57 15pt \"Roboto Mono Medium for Powerline\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.extracting = QtWidgets.QLabel(self.frame_13)
        self.extracting.setStyleSheet("font: 57 13pt \"Roboto Mono Medium for Powerline\";\n"
"color: rgb(87, 227, 137);")
        self.extracting.setText("")
        self.extracting.setAlignment(QtCore.Qt.AlignCenter)
        self.extracting.setObjectName("extracting")
        self.verticalLayout_7.addWidget(self.extracting)
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.link_extract_btn = QtWidgets.QPushButton(self.frame_11)
        self.link_extract_btn.setStyleSheet("background-color: rgb(51, 209, 122);\n"
"color: rgb(255, 255, 255);")
        self.link_extract_btn.setCheckable(True)
        self.link_extract_btn.setChecked(False)
        self.link_extract_btn.setObjectName("link_extract_btn")
        self.verticalLayout_6.addWidget(self.link_extract_btn)
        self.link_cancel_btn = QtWidgets.QPushButton(self.frame_11)
        self.link_cancel_btn.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.link_cancel_btn.setObjectName("link_cancel_btn")
        self.verticalLayout_6.addWidget(self.link_cancel_btn)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.email_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 381))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_14 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_18 = QtWidgets.QFrame(self.frame_14)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_12.setSpacing(1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.save_to_file_btn = QtWidgets.QPushButton(self.frame_18)
        self.save_to_file_btn.setObjectName("save_to_file_btn")
        self.verticalLayout_12.addWidget(self.save_to_file_btn)
        self.horizontalLayout_6.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_14)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_19)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_8.addWidget(self.lineEdit)
        self.path_to_save_btn = QtWidgets.QPushButton(self.frame_19)
        self.path_to_save_btn.setObjectName("path_to_save_btn")
        self.horizontalLayout_8.addWidget(self.path_to_save_btn)
        self.horizontalLayout_6.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_14)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.frame_20)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.depth = QtWidgets.QSpinBox(self.frame_20)
        self.depth.setMinimum(1)
        self.depth.setMaximum(500)
        self.depth.setProperty("value", 100)
        self.depth.setObjectName("depth")
        self.horizontalLayout_7.addWidget(self.depth)
        self.horizontalLayout_6.addWidget(self.frame_20)
        self.verticalLayout_9.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(33)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.frame_17)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.extracted_emails = QtWidgets.QTextEdit(self.frame_17)
        self.extracted_emails.setObjectName("extracted_emails")
        self.verticalLayout_10.addWidget(self.extracted_emails)
        self.horizontalLayout_5.addWidget(self.frame_17)
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.frame_16)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.process_output = QtWidgets.QTextEdit(self.frame_16)
        self.process_output.setReadOnly(True)
        self.process_output.setObjectName("process_output")
        self.verticalLayout_11.addWidget(self.process_output)
        self.horizontalLayout_5.addWidget(self.frame_16)
        self.verticalLayout_9.addWidget(self.frame_15)
        self.verticalLayout.addWidget(self.frame_2)
        self.tabWidget.addTab(self.email_tab, "")
        self.text_tab = QtWidgets.QWidget()
        self.text_tab.setObjectName("text_tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.text_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.text_tab)
        self.frame_3.setMinimumSize(QtCore.QSize(432, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(5, -1, 5, 5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono Medium for Powerline")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 15pt \"Roboto Mono Medium for Powerline\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_13.setSpacing(1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Text_to_extract = QtWidgets.QTextEdit(self.frame_7)
        self.Text_to_extract.setObjectName("Text_to_extract")
        self.verticalLayout_13.addWidget(self.Text_to_extract)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.text_tab)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.text_extract_btn = QtWidgets.QPushButton(self.frame_5)
        self.text_extract_btn.setStyleSheet("background-color: rgb(51, 209, 122);")
        self.text_extract_btn.setObjectName("text_extract_btn")
        self.horizontalLayout_10.addWidget(self.text_extract_btn)
        self.text_save_btn = QtWidgets.QPushButton(self.frame_5)
        self.text_save_btn.setStyleSheet("background-color: rgb(246, 211, 45);")
        self.text_save_btn.setObjectName("text_save_btn")
        self.horizontalLayout_10.addWidget(self.text_save_btn)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(420, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.text_email_extract = QtWidgets.QTextEdit(self.frame_6)
        self.text_email_extract.setObjectName("text_email_extract")
        self.horizontalLayout_9.addWidget(self.text_email_extract)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.tabWidget.addTab(self.text_tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionpath_to_save = QtWidgets.QAction(mainWindow)
        self.actionpath_to_save.setObjectName("actionpath_to_save")

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Email Extractor"))
        self.label_2.setText(_translate("mainWindow", "Paste Link:"))
        self.link_input.setPlaceholderText(_translate("mainWindow", "eg: http://www.google.com,http://facebook.com"))
        self.label_5.setText(_translate("mainWindow", "Note: To extract from more than one link"))
        self.label_6.setText(_translate("mainWindow", "add a comma  \",\"  at the end of the link"))
        self.label_7.setText(_translate("mainWindow", "eg: www.google.com, www.facebook.com"))
        self.label_3.setText(_translate("mainWindow", "Status"))
        self.link_extract_btn.setText(_translate("mainWindow", "Extract"))
        self.link_cancel_btn.setText(_translate("mainWindow", "Cancel"))
        self.save_to_file_btn.setText(_translate("mainWindow", "Save to file"))
        self.path_to_save_btn.setText(_translate("mainWindow", "path to save"))
        self.label_10.setText(_translate("mainWindow", "Link depth"))
        self.label_8.setText(_translate("mainWindow", "Emails extracted"))
        self.extracted_emails.setPlaceholderText(_translate("mainWindow", "all extractd emails will appear here"))
        self.label_9.setText(_translate("mainWindow", "Process Output"))
        self.process_output.setPlaceholderText(_translate("mainWindow", "this shows the process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.email_tab), _translate("mainWindow", "Extract Email From Link"))
        self.label.setText(_translate("mainWindow", "Paste Text"))
        self.text_extract_btn.setText(_translate("mainWindow", "Extract"))
        self.text_save_btn.setText(_translate("mainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.text_tab), _translate("mainWindow", "Extract Email From Text"))
        self.actionpath_to_save.setText(_translate("mainWindow", "path to save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
