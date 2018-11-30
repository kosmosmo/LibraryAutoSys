# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\login2.ui'
#
# Created: Wed Nov 28 11:09:12 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(360, 275)
        self.pushButton_adminlog = QtGui.QPushButton(Login)
        self.pushButton_adminlog.setGeometry(QtCore.QRect(240, 210, 75, 23))
        self.pushButton_adminlog.setObjectName("pushButton_adminlog")
        self.pushButton_adminchange = QtGui.QPushButton(Login)
        self.pushButton_adminchange.setGeometry(QtCore.QRect(240, 240, 75, 23))
        self.pushButton_adminchange.setObjectName("pushButton_adminchange")
        self.lineEdit_user = QtGui.QLineEdit(Login)
        self.lineEdit_user.setGeometry(QtCore.QRect(110, 210, 113, 20))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtGui.QLineEdit(Login)
        self.lineEdit_password.setGeometry(QtCore.QRect(110, 240, 113, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_user = QtGui.QLabel(Login)
        self.label_user.setGeometry(QtCore.QRect(40, 210, 31, 16))
        self.label_user.setScaledContents(False)
        self.label_user.setObjectName("label_user")
        self.label_password = QtGui.QLabel(Login)
        self.label_password.setGeometry(QtCore.QRect(40, 240, 46, 13))
        self.label_password.setObjectName("label_password")
        self.lineEdit_barcode = QtGui.QLineEdit(Login)
        self.lineEdit_barcode.setGeometry(QtCore.QRect(110, 160, 113, 20))
        self.lineEdit_barcode.setObjectName("lineEdit_barcode")
        self.pushButton_readlog = QtGui.QPushButton(Login)
        self.pushButton_readlog.setGeometry(QtCore.QRect(240, 160, 75, 23))
        self.pushButton_readlog.setObjectName("pushButton_readlog")
        self.label_barcode = QtGui.QLabel(Login)
        self.label_barcode.setGeometry(QtCore.QRect(40, 160, 46, 13))
        self.label_barcode.setObjectName("label_barcode")
        self.comboBox_branch = QtGui.QComboBox(Login)
        self.comboBox_branch.setGeometry(QtCore.QRect(110, 120, 201, 22))
        self.comboBox_branch.setObjectName("comboBox_branch")
        self.label_branch = QtGui.QLabel(Login)
        self.label_branch.setGeometry(QtCore.QRect(40, 120, 46, 13))
        self.label_branch.setObjectName("label_branch")
        self.label_image = QtGui.QLabel(Login)
        self.label_image.setGeometry(QtCore.QRect(5, 2, 351, 91))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_adminlog.setText(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_adminchange.setText(QtGui.QApplication.translate("Login", "ChangePW", None, QtGui.QApplication.UnicodeUTF8))
        self.label_user.setText(QtGui.QApplication.translate("Login", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_password.setText(QtGui.QApplication.translate("Login", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_readlog.setText(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_barcode.setText(QtGui.QApplication.translate("Login", "Barcode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_branch.setText(QtGui.QApplication.translate("Login", "Branch", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Login = QtGui.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

