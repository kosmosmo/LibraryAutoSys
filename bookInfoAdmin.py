# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\bookInfoAdmin.ui'
#
# Created: Sat Dec 01 13:50:21 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import DBcall
class Ui_bookInfoAdmin(object):
    def __init__(self,dump):
        self.dump = dump

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 572)
        self.label_ = QtGui.QLabel(Form)
        self.label_.setGeometry(QtCore.QRect(100, 20, 101, 131))
        self.label_.setText("")
        self.label_.setObjectName("label_")
        self.label_ava = QtGui.QLabel(Form)
        self.label_ava.setGeometry(QtCore.QRect(100, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_ava.setFont(font)
        self.label_ava.setObjectName("label_ava")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 46, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_isbn = QtGui.QLineEdit(Form)
        self.lineEdit_isbn.setGeometry(QtCore.QRect(90, 210, 171, 20))
        self.lineEdit_isbn.setObjectName("lineEdit_isbn")
        self.lineEdit_title = QtGui.QLineEdit(Form)
        self.lineEdit_title.setGeometry(QtCore.QRect(90, 240, 171, 20))
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 46, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_author = QtGui.QLineEdit(Form)
        self.lineEdit_author.setGeometry(QtCore.QRect(90, 270, 171, 20))
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 300, 46, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_publisher = QtGui.QLineEdit(Form)
        self.lineEdit_publisher.setGeometry(QtCore.QRect(90, 300, 171, 20))
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 270, 46, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 330, 46, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_lang = QtGui.QLineEdit(Form)
        self.lineEdit_lang.setGeometry(QtCore.QRect(90, 330, 171, 20))
        self.lineEdit_lang.setObjectName("lineEdit_lang")
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 360, 46, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_year = QtGui.QLineEdit(Form)
        self.lineEdit_year.setGeometry(QtCore.QRect(90, 360, 171, 20))
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.textEdit_log = QtGui.QTextEdit(Form)
        self.textEdit_log.setGeometry(QtCore.QRect(20, 390, 291, 171))
        self.textEdit_log.setObjectName("textEdit_log")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        p, lan, ti, au, isbn, y = self.dump
        self.label_.setPixmap("repository/cover/"+isbn+".jpg")
        self.label_.setScaledContents(True)
        self.lineEdit_isbn.setText(isbn)
        self.lineEdit_title.setText(ti)
        self.lineEdit_author.setText(au)
        self.lineEdit_publisher.setText(p)
        self.lineEdit_lang.setText(lan)
        self.lineEdit_year.setText(y)
        sql = DBcall.Mysql()
        ava = sql.getBookAvi(self.dump[-2])
        self.label_ava.setText(str(len(ava[0])) +"/"+ str(len(ava[1])) + " Avaiable!!")
        path = "logs/bookLog/" + isbn + ".txt"
        text = open(path).read()
        self.textEdit_log.setPlainText(text)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ava.setText(QtGui.QApplication.translate("Form", "0/0 Avaiable!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "ISBN:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Publisher:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Author:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Year:", None, QtGui.QApplication.UnicodeUTF8))

