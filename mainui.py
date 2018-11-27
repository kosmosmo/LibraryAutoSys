# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\login.ui'
#
# Created: Tue Nov 27 17:21:01 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(360, 275)
        self.pushButton_adminlog = QtGui.QPushButton(Login)
        self.pushButton_adminlog.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.pushButton_adminlog.setObjectName("pushButton_adminlog")
        self.pushButton_adminchange = QtGui.QPushButton(Login)
        self.pushButton_adminchange.setGeometry(QtCore.QRect(240, 180, 75, 23))
        self.pushButton_adminchange.setObjectName("pushButton_adminchange")
        self.lineEdit_user = QtGui.QLineEdit(Login)
        self.lineEdit_user.setGeometry(QtCore.QRect(110, 150, 113, 20))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtGui.QLineEdit(Login)
        self.lineEdit_password.setGeometry(QtCore.QRect(110, 180, 113, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_user = QtGui.QLabel(Login)
        self.label_user.setGeometry(QtCore.QRect(40, 150, 31, 16))
        self.label_user.setScaledContents(False)
        self.label_user.setObjectName("label_user")
        self.label_password = QtGui.QLabel(Login)
        self.label_password.setGeometry(QtCore.QRect(40, 180, 46, 13))
        self.label_password.setObjectName("label_password")
        self.lineEdit_barcode = QtGui.QLineEdit(Login)
        self.lineEdit_barcode.setGeometry(QtCore.QRect(110, 60, 113, 20))
        self.lineEdit_barcode.setObjectName("lineEdit_barcode")
        self.pushButton_readlog = QtGui.QPushButton(Login)
        self.pushButton_readlog.setGeometry(QtCore.QRect(240, 60, 75, 23))
        self.pushButton_readlog.setObjectName("pushButton_readlog")
        self.label_barcode = QtGui.QLabel(Login)
        self.label_barcode.setGeometry(QtCore.QRect(40, 60, 46, 13))
        self.label_barcode.setObjectName("label_barcode")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_adminlog.setText(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_adminchange.setText(QtGui.QApplication.translate("Login", "ChangePW", None, QtGui.QApplication.UnicodeUTF8))
        self.label_user.setText(QtGui.QApplication.translate("Login", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_password.setText(QtGui.QApplication.translate("Login", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_readlog.setText(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_barcode.setText(QtGui.QApplication.translate("Login", "Barcode", None, QtGui.QApplication.UnicodeUTF8))



