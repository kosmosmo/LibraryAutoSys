from PySide.QtCore import *
from PySide.QtGui import *
from changeui import Ui_ChangePassword
from adminWin import Ui_adminWin
import sys
import Authentication
import mainui
import changeui

class MainDialog(QDialog,mainui.Ui_Login):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)
        self.setupUi(self)
        self.pushButton_adminchange.clicked.connect(self.openChange)
        self.pushButton_adminlog.clicked.connect(self.checking)

    def openAdmin(self):
        self.window = QMainWindow()
        self.ui = Ui_adminWin()
        self.ui.setupUi(self.window)
        self.window.show()

    def openChange(self):
        self.window = QMainWindow()
        self.ui = Ui_ChangePassword()
        self.ui.setupUi(self.window)
        self.window.show()

    def checking(self):
        auth = Authentication.Authentication()
        res = auth.checkpw(self.lineEdit_user.text(),self.lineEdit_password.text())
        if not res:
            QMessageBox.information(self,"Nope!","User name or password not correct")
        else:
            self.openAdmin()
            file = open("cache/admin.txt", "w")
            file.write(self.lineEdit_user.text())
            file.close()
            self.lineEdit_password.clear()



app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()