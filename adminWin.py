# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\adminWin.ui'
#
# Created: Wed Nov 28 12:06:17 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import Authentication

class Ui_adminWin(object):
    def setupUi(self, adminWin):
        adminWin.setObjectName("adminWin")
        adminWin.resize(620, 632)
        self.listWidget_reader = QtGui.QListWidget(adminWin)
        self.listWidget_reader.setGeometry(QtCore.QRect(10, 50, 341, 511))
        self.listWidget_reader.setObjectName("listWidget_reader")
        self.lineEdit_search = QtGui.QLineEdit(adminWin)
        self.lineEdit_search.setGeometry(QtCore.QRect(50, 20, 301, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.label_search = QtGui.QLabel(adminWin)
        self.label_search.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_search.setObjectName("label_search")
        self.textEdit_history = QtGui.QTextEdit(adminWin)
        self.textEdit_history.setGeometry(QtCore.QRect(370, 50, 231, 141))
        self.textEdit_history.setObjectName("textEdit_history")
        self.pushButton_get = QtGui.QPushButton(adminWin)
        self.pushButton_get.setGeometry(QtCore.QRect(190, 580, 131, 23))
        self.pushButton_get.setObjectName("pushButton_get")
        self.pushButton_back = QtGui.QPushButton(adminWin)
        self.pushButton_back.setGeometry(QtCore.QRect(30, 580, 131, 23))
        self.pushButton_back.setObjectName("pushButton_back")
        self.lineEdit_isbn = QtGui.QLineEdit(adminWin)
        self.lineEdit_isbn.setGeometry(QtCore.QRect(370, 230, 231, 21))
        self.lineEdit_isbn.setObjectName("lineEdit_isbn")
        self.pushButton_bookstatus = QtGui.QPushButton(adminWin)
        self.pushButton_bookstatus.setGeometry(QtCore.QRect(490, 270, 111, 21))
        self.pushButton_bookstatus.setObjectName("pushButton_bookstatus")
        self.pushButton_10borrow = QtGui.QPushButton(adminWin)
        self.pushButton_10borrow.setGeometry(QtCore.QRect(370, 310, 111, 23))
        self.pushButton_10borrow.setObjectName("pushButton_10borrow")
        self.pushButton_10book = QtGui.QPushButton(adminWin)
        self.pushButton_10book.setGeometry(QtCore.QRect(490, 310, 111, 23))
        self.pushButton_10book.setObjectName("pushButton_10book")
        self.lineEdit_user = QtGui.QLineEdit(adminWin)
        self.lineEdit_user.setGeometry(QtCore.QRect(370, 370, 111, 21))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_pw = QtGui.QLineEdit(adminWin)
        self.lineEdit_pw.setGeometry(QtCore.QRect(490, 370, 111, 21))
        self.lineEdit_pw.setObjectName("lineEdit_pw")
        self.label_user = QtGui.QLabel(adminWin)
        self.label_user.setGeometry(QtCore.QRect(370, 350, 41, 16))
        self.label_user.setObjectName("label_user")
        self.label_pw = QtGui.QLabel(adminWin)
        self.label_pw.setGeometry(QtCore.QRect(490, 350, 61, 16))
        self.label_pw.setObjectName("label_pw")
        self.pushButton_addadmin = QtGui.QPushButton(adminWin)
        self.pushButton_addadmin.setGeometry(QtCore.QRect(490, 400, 111, 23))
        self.pushButton_addadmin.setObjectName("pushButton_addadmin")
        self.lineEdit_name = QtGui.QLineEdit(adminWin)
        self.lineEdit_name.setGeometry(QtCore.QRect(370, 440, 231, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtGui.QLabel(adminWin)
        self.label_name.setGeometry(QtCore.QRect(370, 420, 41, 16))
        self.label_name.setObjectName("label_name")
        self.label_add = QtGui.QLabel(adminWin)
        self.label_add.setGeometry(QtCore.QRect(370, 470, 71, 16))
        self.label_add.setObjectName("label_add")
        self.lineEdit_add = QtGui.QLineEdit(adminWin)
        self.lineEdit_add.setGeometry(QtCore.QRect(370, 490, 231, 21))
        self.lineEdit_add.setObjectName("lineEdit_add")
        self.label_phone = QtGui.QLabel(adminWin)
        self.label_phone.setGeometry(QtCore.QRect(370, 520, 41, 16))
        self.label_phone.setObjectName("label_phone")
        self.lineEdit_phone = QtGui.QLineEdit(adminWin)
        self.lineEdit_phone.setGeometry(QtCore.QRect(370, 540, 231, 21))
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.pushButton_addreader = QtGui.QPushButton(adminWin)
        self.pushButton_addreader.setGeometry(QtCore.QRect(490, 580, 111, 23))
        self.pushButton_addreader.setObjectName("pushButton_addreader")
        self.label_history = QtGui.QLabel(adminWin)
        self.label_history.setGeometry(QtCore.QRect(370, 20, 41, 16))
        self.label_history.setObjectName("label_history")
        self.pushButton_booklog = QtGui.QPushButton(adminWin)
        self.pushButton_booklog.setGeometry(QtCore.QRect(370, 270, 111, 21))
        self.pushButton_booklog.setObjectName("pushButton_booklog")
        self.label_isbn = QtGui.QLabel(adminWin)
        self.label_isbn.setGeometry(QtCore.QRect(370, 210, 41, 16))
        self.label_isbn.setObjectName("label_isbn")

        self.retranslateUi(adminWin)
        QtCore.QMetaObject.connectSlotsByName(adminWin)

    def retranslateUi(self, adminWin):
        adminWin.setWindowTitle(QtGui.QApplication.translate("adminWin", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_search.setText(QtGui.QApplication.translate("adminWin", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_get.setText(QtGui.QApplication.translate("adminWin", "Get", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_back.setText(QtGui.QApplication.translate("adminWin", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bookstatus.setText(QtGui.QApplication.translate("adminWin", "Book status", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10borrow.setText(QtGui.QApplication.translate("adminWin", "Top 10 borrowers", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10book.setText(QtGui.QApplication.translate("adminWin", "Top 10 books", None, QtGui.QApplication.UnicodeUTF8))
        self.label_user.setText(QtGui.QApplication.translate("adminWin", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pw.setText(QtGui.QApplication.translate("adminWin", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_addadmin.setText(QtGui.QApplication.translate("adminWin", "Add new admin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_name.setText(QtGui.QApplication.translate("adminWin", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_add.setText(QtGui.QApplication.translate("adminWin", "Address:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_phone.setText(QtGui.QApplication.translate("adminWin", "Phone:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_addreader.setText(QtGui.QApplication.translate("adminWin", "Add new reader", None, QtGui.QApplication.UnicodeUTF8))
        self.label_history.setText(QtGui.QApplication.translate("adminWin", "History:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_booklog.setText(QtGui.QApplication.translate("adminWin", "Book Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label_isbn.setText(QtGui.QApplication.translate("adminWin", "ISBN:", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton_addadmin.clicked.connect(self.createadmin)

    def createadmin(self):
        auth = Authentication.Authentication()
        user = self.lineEdit_user.text()
        pw = self.lineEdit_pw.text()
        res = False
        if not user and not pw:
            res = auth.createAdmin(user,pw)
        if not res:
            self.textEdit_history.setText("Create admin "+ user +" sccussed!")
        else:
            self.textEdit_history.setText("Create admin "+ user +" Failed!")


