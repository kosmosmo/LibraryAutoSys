# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\addCopy.ui'
#
# Created: Fri Nov 30 21:25:43 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import DBcall
import datetime

class Ui_AddCopy(object):
    def __init__(self,ISBN):
        self.ISBN = ISBN

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(317, 319)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 260, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 260, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 40, 101, 131))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_title = QtGui.QLineEdit(Form)
        self.lineEdit_title.setGeometry(QtCore.QRect(90, 190, 171, 20))
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 46, 21))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.label.setPixmap("repository/cover/" + self.ISBN + ".jpg")
        self.lineEdit_title.setText(self.ISBN)
        self.pushButton.clicked.connect(self.addCopy)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Confirm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Add new copy?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Title:", None, QtGui.QApplication.UnicodeUTF8))

    def addCopy(self):
        sql = DBcall.Mysql()
        admin = open("cache/admin.txt").read()
        ISBN = self.ISBN
        file = open('logs/bookLog/' + ISBN + '.txt', 'a')
        info = sql.addcopy(ISBN)
        file.write("\n")
        file.write(str(datetime.datetime.now())[:-7] + '_' + "Book Copy " + info + " added by " + admin)
        file.close()
        self.label_2.setText("Copy " + info + " add")



