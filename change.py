from PySide.QtCore import *
from PySide.QtGui import *
import sys
import Authentication
import changeui

class MainDialog(QDialog,changeui.Ui_ChangePassword):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()