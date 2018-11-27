from PySide.QtCore import *
from PySide.QtGui import *
import sys
import Authentication

import mainui

class MainDialog(QDialog,mainui.Ui_Login):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButton_adminlog, SIGNAL("clicked()"),self.checking)

    def checking(self):
        auth = Authentication.Authentication()
        res = auth.checkpw(self.lineEdit_user.text(),self.lineEdit_password.text())
        if not res:
            QMessageBox.information(self,"Nope!","User name or password not correct")


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()