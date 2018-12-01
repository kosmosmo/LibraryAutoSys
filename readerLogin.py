# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\momo\PycharmProjects\LibraryAutoSys\qtshit\readerLogin.ui'
#
# Created: Fri Nov 30 13:44:24 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import DBcall
import Books
import os
import DBcall
import datetime
from bookInfoReader import Ui_bookInfoReader

class Ui_readerLogin(object):
    def __init__(self,id):
        self.id = id
        sql = DBcall.Mysql()
        self.books = sql.getAllBook()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(814, 563)
        self.label_profile = QtGui.QLabel(Form)
        self.label_profile.setGeometry(QtCore.QRect(30, 40, 131, 131))
        self.label_profile.setText("")
        self.label_profile.setObjectName("label_profile")
        self.lineEdit_name = QtGui.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(80, 190, 131, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtGui.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(30, 190, 46, 21))
        self.label_name.setObjectName("label_name")
        self.lineEdit_add = QtGui.QLineEdit(Form)
        self.lineEdit_add.setGeometry(QtCore.QRect(80, 230, 131, 20))
        self.lineEdit_add.setObjectName("lineEdit_add")
        self.label_add = QtGui.QLabel(Form)
        self.label_add.setGeometry(QtCore.QRect(30, 230, 46, 21))
        self.label_add.setObjectName("label_add")
        self.lineEdit_phone = QtGui.QLineEdit(Form)
        self.lineEdit_phone.setGeometry(QtCore.QRect(80, 270, 131, 20))
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.label_phone = QtGui.QLabel(Form)
        self.label_phone.setGeometry(QtCore.QRect(30, 270, 46, 21))
        self.label_phone.setObjectName("label_phone")
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(480, 70, 311, 471))
        self.listWidget.setObjectName("listWidget")
        self.label_name_search = QtGui.QLabel(Form)
        self.label_name_search.setGeometry(QtCore.QRect(480, 40, 46, 21))
        self.label_name_search.setObjectName("label_name_search")
        self.lineEdit_search = QtGui.QLineEdit(Form)
        self.lineEdit_search.setGeometry(QtCore.QRect(530, 40, 171, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_bookinfo = QtGui.QPushButton(Form)
        self.pushButton_bookinfo.setGeometry(QtCore.QRect(710, 40, 81, 23))
        self.pushButton_bookinfo.setObjectName("pushButton_bookinfo")
        self.textEdit_info = QtGui.QTextEdit(Form)
        self.textEdit_info.setGeometry(QtCore.QRect(230, 160, 231, 381))
        self.textEdit_info.setObjectName("textEdit_info")
        self.lineEdit_isbn = QtGui.QLineEdit(Form)
        self.lineEdit_isbn.setGeometry(QtCore.QRect(290, 40, 171, 20))
        self.lineEdit_isbn.setObjectName("lineEdit_isbn")
        self.label_isbn = QtGui.QLabel(Form)
        self.label_isbn.setGeometry(QtCore.QRect(230, 40, 46, 21))
        self.label_isbn.setObjectName("label_isbn")
        self.pushButton_check = QtGui.QPushButton(Form)
        self.pushButton_check.setGeometry(QtCore.QRect(360, 70, 101, 23))
        self.pushButton_check.setObjectName("pushButton_check")
        self.pushButton_pick = QtGui.QPushButton(Form)
        self.pushButton_pick.setGeometry(QtCore.QRect(230, 70, 101, 23))
        self.pushButton_pick.setObjectName("pushButton_pick")
        self.pushButton_res = QtGui.QPushButton(Form)
        self.pushButton_res.setGeometry(QtCore.QRect(230, 100, 101, 23))
        self.pushButton_res.setObjectName("pushButton_res")
        self.pushButton_ret = QtGui.QPushButton(Form)
        self.pushButton_ret.setGeometry(QtCore.QRect(360, 100, 101, 23))
        self.pushButton_ret.setObjectName("pushButton_ret")
        self.pushButton_reRes = QtGui.QPushButton(Form)
        self.pushButton_reRes.setGeometry(QtCore.QRect(100, 310, 111, 23))
        self.pushButton_reRes.setObjectName("pushButton_reRes")
        self.pushButton_reBor = QtGui.QPushButton(Form)
        self.pushButton_reBor.setGeometry(QtCore.QRect(100, 350, 111, 23))
        self.pushButton_reBor.setObjectName("pushButton_reBor")
        self.pushButton_dummy01 = QtGui.QPushButton(Form)
        self.pushButton_dummy01.setGeometry(QtCore.QRect(130, 500, 71, 23))
        self.pushButton_dummy01.setObjectName("pushButton_dummy01")
        self.pushButton_dummy02 = QtGui.QPushButton(Form)
        self.pushButton_dummy02.setGeometry(QtCore.QRect(30, 500, 71, 23))
        self.pushButton_dummy02.setObjectName("pushButton_dummy02")
        self.pushButton_getAuth = QtGui.QPushButton(Form)
        self.pushButton_getAuth.setGeometry(QtCore.QRect(130, 460, 71, 23))
        self.pushButton_getAuth.setObjectName("pushButton_getAuth")
        self.pushButton_getPub = QtGui.QPushButton(Form)
        self.pushButton_getPub.setGeometry(QtCore.QRect(30, 460, 71, 23))
        self.pushButton_getPub.setObjectName("pushButton_getPub")
        self.lineEdit_author_or_pub = QtGui.QLineEdit(Form)
        self.lineEdit_author_or_pub.setGeometry(QtCore.QRect(30, 420, 171, 20))
        self.lineEdit_author_or_pub.setObjectName("lineEdit_author_or_pub")
        self.label_author_or_pub = QtGui.QLabel(Form)
        self.label_author_or_pub.setGeometry(QtCore.QRect(30, 390, 161, 21))
        self.label_author_or_pub.setObjectName("label_author_or_pub")
        self.pushButton_fine = QtGui.QPushButton(Form)
        self.pushButton_fine.setGeometry(QtCore.QRect(360, 130, 101, 23))
        self.pushButton_fine.setObjectName("pushButton_fine")
        self.pushButton_dummy03 = QtGui.QPushButton(Form)
        self.pushButton_dummy03.setGeometry(QtCore.QRect(230, 130, 101, 23))
        self.pushButton_dummy03.setObjectName("pushButton_dummy03")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        path = "logs/readerLog/" + self.id + ".txt"
        file = open(path).readlines()
        self.lineEdit_name.setText(file[1])
        self.lineEdit_add.setText(file[2])
        self.lineEdit_phone.setText(file[3])
        self.lineEdit_name.setEnabled(False)
        self.lineEdit_phone.setEnabled(False)
        self.lineEdit_add.setEnabled(False)
        image = "repository/pictures/" + self.id + ".jpg"
        ex = os.path.exists(image)
        if not ex:
            image = "repository/pictures/0000000.jpg"
            self.label_profile.setPixmap(image)
            self.label_profile.setScaledContents(True)
        else:
            self.label_profile.setPixmap(image)
            self.label_profile.setScaledContents(True)


        for item in self.books:
            self.listWidget.addItem(item)
        self.lineEdit_search.textChanged.connect(self.buildBookList)

        self.pushButton_check.clicked.connect(self.checkOutt)

        self.pushButton_reBor.clicked.connect(self.getBorrowed)
        self.pushButton_reRes.clicked.connect(self.getReserved)
        self.pushButton_res.clicked.connect(self.makeRserved)

        self.pushButton_ret.clicked.connect(self.returnBook)
        self.pushButton_pick.clicked.connect(self.pickBook)
        self.displayReserve()
        self.listWidget.itemClicked.connect(self.updateISBN)
        self.pushButton_fine.clicked.connect(self.computeFine)
        self.pushButton_bookinfo.clicked.connect(self.bookInfo)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_name.setText(QtGui.QApplication.translate("Form", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_add.setText(QtGui.QApplication.translate("Form", "Address:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_phone.setText(QtGui.QApplication.translate("Form", "Phone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_name_search.setText(QtGui.QApplication.translate("Form", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bookinfo.setText(QtGui.QApplication.translate("Form", "Book Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_isbn.setText(QtGui.QApplication.translate("Form", "ISBN:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_check.setText(QtGui.QApplication.translate("Form", "Check Out", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pick.setText(QtGui.QApplication.translate("Form", "Pick Up", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_res.setText(QtGui.QApplication.translate("Form", "Reserve", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ret.setText(QtGui.QApplication.translate("Form", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reRes.setText(QtGui.QApplication.translate("Form", "Reader Reserved", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reBor.setText(QtGui.QApplication.translate("Form", "Reader Borrowed", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_dummy01.setText(QtGui.QApplication.translate("Form", "Dummy01", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_dummy02.setText(QtGui.QApplication.translate("Form", "Dummy02", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_getAuth.setText(QtGui.QApplication.translate("Form", "Get Author", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_getPub.setText(QtGui.QApplication.translate("Form", "Get Publisher", None, QtGui.QApplication.UnicodeUTF8))
        self.label_author_or_pub.setText(QtGui.QApplication.translate("Form", "Search by Author or Publisher:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_fine.setText(QtGui.QApplication.translate("Form", "Compute Fine", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_dummy03.setText(QtGui.QApplication.translate("Form", "Dummy03", None, QtGui.QApplication.UnicodeUTF8))

    def buildBookList(self):
        self.listWidget.clear()
        searchPattern = self.lineEdit_search.text().lower()
        for read in self.books:
            name = read
            if searchPattern in name.lower():
                item = QtGui.QListWidgetItem(name)
                item.setData(32,read)
                self.listWidget.addItem(item)
        self.listWidget.sortItems()

    def pickUp(self):
        book = Books.BookManagement()
        ISBN = self.lineEdit_isbn.text()
        book.pickUp(ISBN,self.id)

    def checkOutt(self):
        sql = DBcall.Mysql()
        book = Books.BookManagement()
        ISBN = self.lineEdit_isbn.text()
        if len(sql.bookBorrow(self.id)) >= 10:
            self.textEdit_info.setPlainText("Check out failed! More than 10 books were borrowed by the reader already!")
        elif len(sql.getBookAvi(ISBN)[0]) == 0:
            self.textEdit_info.setPlainText("No book available at the moment")
        else:
            book.checkOut(ISBN, self.id)
            file = open('logs/bookLog/' + ISBN + '.txt', 'a')
            file.write("\n")
            file.write(str(datetime.datetime.now())[:-7] + '_' + "Book Borrowed by " + self.id)
            file.close()

            file = open('logs/readerLog/' + self.id + '.txt', 'a')
            file.write("\n")
            file.write(str(datetime.datetime.now())[:-7] + '_' + "Book " + ISBN +" Borrowed")
            file.close()
            self.textEdit_info.setPlainText("Book borrowed")

    def getBorrowed(self):
        sql = DBcall.Mysql()
        bor = sql.getBorrowed(self.id)
        res = []
        for book in bor:
            res.append(book +'_' +sql.getBookTile(book))
        self.textEdit_info.clear()
        self.textEdit_info.append("List of Books User " + self.id + " Borrowed:\n")
        for item in res:
            self.textEdit_info.append(item)
        return res

    def getReserved(self):
        sql = DBcall.Mysql()
        rev = sql.getReserved(self.id)
        res = []
        for book in rev:
            res.append(book +'_' +sql.getBookTile(book))
        self.textEdit_info.clear()
        self.textEdit_info.append("List of Books User " + self.id + " Reserved:\n")
        for item in res:
            self.textEdit_info.append(item)
        return res

    def makeRserved(self):
        sql = DBcall.Mysql()
        ISBN = self.lineEdit_isbn.text()
        if len(sql.bookReserve(self.id)) >= 10:
            self.textEdit_info.setPlainText("Reserve failed! More than 10 books were reserved by the reader already!")
        elif len(sql.getBookAvi(ISBN)[0]) != 0:
            self.textEdit_info.setPlainText("Can not make reserve! Book still avaviable for check out")
        else:
            sql.makeReserve(ISBN,self.id)
            self.textEdit_info.setPlainText("Reserved!")

    def returnBook(self):
        sql = DBcall.Mysql()
        ISBN = self.lineEdit_isbn.text()
        try:
            sql.returnBook(ISBN,self.id)
            self.textEdit_info.setPlainText("Returned!")
        except:
            self.textEdit_info.setPlainText("Return Failed!")

    def pickBook(self):
        sql = DBcall.Mysql()
        ISBN = self.lineEdit_isbn.text()
        try:
            temp = sql.checkHold(ISBN, self.id)
            print temp
            if not temp:
                self.textEdit_info.setPlainText("Pick Up not ready!")
            else:
                sql.pickUp(ISBN,self.id)
                self.textEdit_info.setPlainText("Picked Up!")
        except:
            self.textEdit_info.setPlainText("Picked Up Failed!")

    def displayReserve(self):
        sql = DBcall.Mysql()
        self.textEdit_info.setPlainText("Book are ready to pickUp:")
        ready = sql.getReserveInfo(self.id)[0]
        notready = sql.getReserveInfo(self.id)[1]
        for item in ready:
            self.textEdit_info.append(item + '_' +sql.getBookTile(item))
        self.textEdit_info.append("\n")
        self.textEdit_info.append("Book are not ready to pickUp yet:")
        for item in notready:
            self.textEdit_info.append(item + '_' +sql.getBookTile(item))

    def updateISBN(self):
        self.lineEdit_isbn.clear()
        nisbn = self.listWidget.currentItem().text()[:13]
        self.lineEdit_isbn.setText(nisbn)

    def computeFine(self):
        sql = DBcall.Mysql()
        ISBN = self.lineEdit_isbn.text()
        fine = sql.computeFine(ISBN,self.id)
        self.textEdit_info.setPlainText("The fine will be "+str(fine) + " cents")

    def bookInfo(self):
        sql = DBcall.Mysql()
        ISBN = self.listWidget.currentItem().text()[:13]
        dump = sql.retriveBook(ISBN)
        self.window = QtGui.QMainWindow()
        self.ui = Ui_bookInfoReader(dump)
        self.ui.setupUi(self.window)
        self.window.show()