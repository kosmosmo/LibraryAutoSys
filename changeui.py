# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\change.ui'
#
# Created: Wed Nov 28 00:53:15 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import Authentication

class Ui_ChangePassword(object):
    def setupUi(self, ChangePassword):
        ChangePassword.setObjectName("ChangePassword")
        ChangePassword.resize(310, 248)
        self.lineEdit_user = QtGui.QLineEdit(ChangePassword)
        self.lineEdit_user.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_oldpw = QtGui.QLineEdit(ChangePassword)
        self.lineEdit_oldpw.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.lineEdit_oldpw.setObjectName("lineEdit_oldpw")
        self.lineEdit_newpw = QtGui.QLineEdit(ChangePassword)
        self.lineEdit_newpw.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.lineEdit_newpw.setObjectName("lineEdit_newpw")
        self.label_user = QtGui.QLabel(ChangePassword)
        self.label_user.setGeometry(QtCore.QRect(60, 60, 46, 13))
        self.label_user.setObjectName("label_user")
        self.label_oldpw = QtGui.QLabel(ChangePassword)
        self.label_oldpw.setGeometry(QtCore.QRect(60, 100, 46, 13))
        self.label_oldpw.setObjectName("label_oldpw")
        self.label_newpw = QtGui.QLabel(ChangePassword)
        self.label_newpw.setGeometry(QtCore.QRect(60, 140, 46, 13))
        self.label_newpw.setObjectName("label_newpw")
        self.pushButton_change = QtGui.QPushButton(ChangePassword)
        self.pushButton_change.setGeometry(QtCore.QRect(120, 180, 75, 23))
        self.pushButton_change.setObjectName("pushButton_change")
        self.label_st = QtGui.QLabel(ChangePassword)
        self.label_st.setGeometry(QtCore.QRect(80, 20, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.label_st.setFont(font)
        self.label_st.setObjectName("label_st")

        self.retranslateUi(ChangePassword)
        QtCore.QMetaObject.connectSlotsByName(ChangePassword)

    def retranslateUi(self, ChangePassword):
        ChangePassword.setWindowTitle(QtGui.QApplication.translate("ChangePassword", "ChangePW", None, QtGui.QApplication.UnicodeUTF8))
        self.label_user.setText(QtGui.QApplication.translate("ChangePassword", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_oldpw.setText(QtGui.QApplication.translate("ChangePassword", "Old PW", None, QtGui.QApplication.UnicodeUTF8))
        self.label_newpw.setText(QtGui.QApplication.translate("ChangePassword", "New PW", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_change.setText(QtGui.QApplication.translate("ChangePassword", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.label_st.setText(QtGui.QApplication.translate("ChangePassword", "", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_change.clicked.connect(self.change)

    def change(self):
        auth = Authentication.Authentication()
        res = auth.changePW(self.lineEdit_user.text(),self.lineEdit_oldpw.text(),self.lineEdit_newpw.text())
        if res:
            self.label_st.setText("SUCCESSED!!")
        else:
            self.label_st.setText("FAILED!")


