from PySide.QtCore import *
from PySide.QtGui import *
from changeui import Ui_ChangePassword
import sys
import Authentication
import mainui
import changeui

class MainDialog(QDialog,mainui.Ui_Login):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)
        self.setupUi(self)
        self.pushButton_adminchange.clicked.connect(self.openChange)
        self.connect(self.pushButton_adminlog, SIGNAL("clicked()"),self.checking)


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



app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()