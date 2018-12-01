# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\bookInfoReader.ui'
#
# Created: Sat Dec 01 13:08:35 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(317, 454)
        self.label_cover = QtGui.QLabel(Form)
        self.label_cover.setGeometry(QtCore.QRect(100, 40, 101, 131))
        self.label_cover.setText("")
        self.label_cover.setObjectName("label_cover")
        self.label_ava = QtGui.QLabel(Form)
        self.label_ava.setGeometry(QtCore.QRect(100, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_ava.setFont(font)
        self.label_ava.setObjectName("label_ava")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 46, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_isbn = QtGui.QLineEdit(Form)
        self.lineEdit_isbn.setGeometry(QtCore.QRect(90, 230, 171, 20))
        self.lineEdit_isbn.setObjectName("lineEdit_isbn")
        self.lineEdit_title = QtGui.QLineEdit(Form)
        self.lineEdit_title.setGeometry(QtCore.QRect(90, 260, 171, 20))
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 46, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_author = QtGui.QLineEdit(Form)
        self.lineEdit_author.setGeometry(QtCore.QRect(90, 290, 171, 20))
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 320, 46, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_publisher = QtGui.QLineEdit(Form)
        self.lineEdit_publisher.setGeometry(QtCore.QRect(90, 320, 171, 20))
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 290, 46, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 350, 46, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_lang = QtGui.QLineEdit(Form)
        self.lineEdit_lang.setGeometry(QtCore.QRect(90, 350, 171, 20))
        self.lineEdit_lang.setObjectName("lineEdit_lang")
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 380, 46, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_year = QtGui.QLineEdit(Form)
        self.lineEdit_year.setGeometry(QtCore.QRect(90, 380, 171, 20))
        self.lineEdit_year.setObjectName("lineEdit_year")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ava.setText(QtGui.QApplication.translate("Form", "0/0 Avaiable!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "ISBN:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Publisher:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Author:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Year:", None, QtGui.QApplication.UnicodeUTF8))

