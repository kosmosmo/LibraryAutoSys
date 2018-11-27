import os,DBcall
class BookManagement:
    def searchID(self,ISBN):
        return

    def searchTitle(self,title):
        return

    def searchPN(self,pName):
        return

    def checkOut(self,ISBN,Borrow):
        json = DBcall.Json()
        json.checkOut(ISBN,Borrow)
        return

    def addBook(self,ISBN):
        dir = "repository/book/" + ISBN
        json = DBcall.Json()
        if os.path.isdir(dir):json.addcopy(ISBN)
        else:json.addbook(ISBN)

    def returnBook(self,ISBN,Borrow):
        json = DBcall.Json()
        json.returnBook(ISBN,Borrow)


    def reserve(self,ISBN):
        return

a = BookManagement()
a.addBook("9780345476722")
a.addBook("9780345476722")
a.checkOut("9780345476722","123")
a.checkOut("9780345476722","321")
a.returnBook("9780345476722","321")
