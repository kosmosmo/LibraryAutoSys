# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\readerPop.ui'
#
# Created: Fri Nov 30 11:26:02 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(509, 570)
        self.label_profile = QtGui.QLabel(Form)
        self.label_profile.setGeometry(QtCore.QRect(30, 40, 131, 131))
        self.label_profile.setText("")
        self.label_profile.setObjectName("label_profile")
        self.lineEdit_name = QtGui.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(90, 190, 221, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtGui.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(30, 190, 46, 21))
        self.label_name.setObjectName("label_name")
        self.lineEdit_add = QtGui.QLineEdit(Form)
        self.lineEdit_add.setGeometry(QtCore.QRect(90, 220, 221, 20))
        self.lineEdit_add.setObjectName("lineEdit_add")
        self.label_add = QtGui.QLabel(Form)
        self.label_add.setGeometry(QtCore.QRect(30, 220, 46, 21))
        self.label_add.setObjectName("label_add")
        self.lineEdit_phone = QtGui.QLineEdit(Form)
        self.lineEdit_phone.setGeometry(QtCore.QRect(90, 250, 221, 20))
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.label_phone = QtGui.QLabel(Form)
        self.label_phone.setGeometry(QtCore.QRect(30, 250, 46, 21))
        self.label_phone.setObjectName("label_phone")
        self.lineEdit_logs = QtGui.QLineEdit(Form)
        self.lineEdit_logs.setGeometry(QtCore.QRect(30, 310, 451, 221))
        self.lineEdit_logs.setObjectName("lineEdit_logs")
        self.label_logs = QtGui.QLabel(Form)
        self.label_logs.setGeometry(QtCore.QRect(30, 280, 46, 21))
        self.label_logs.setObjectName("label_logs")
        self.pushButton_clear = QtGui.QPushButton(Form)
        self.pushButton_clear.setGeometry(QtCore.QRect(400, 280, 75, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_name.setText(QtGui.QApplication.translate("Form", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_add.setText(QtGui.QApplication.translate("Form", "Address:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_phone.setText(QtGui.QApplication.translate("Form", "Phone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_logs.setText(QtGui.QApplication.translate("Form", "Logs:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_clear.setText(QtGui.QApplication.translate("Form", "ClearLog", None, QtGui.QApplication.UnicodeUTF8))

