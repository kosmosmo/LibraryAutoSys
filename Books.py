import os,DBcall
class BookManagement:
    def checkOut(self,ISBN,Borrow):
        sql = DBcall.Mysql()
        return sql.checkOut(ISBN,Borrow)

    def addBook(self,ISBN):
        sql = DBcall.Mysql()
        temp = sql.checkBook(ISBN)
        if temp:
            info = sql.addcopy(ISBN)
        else:
            info = sql.addbook(ISBN)
        return info

    def returnBook(self,ISBN,Borrow):
        sql = DBcall.Mysql()
        sql.returnBook(ISBN,Borrow)

    def reserve(self,ISBN):
        return

