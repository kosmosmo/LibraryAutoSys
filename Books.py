import os,DBcall,datetime
class BookManagement:
    def checkOut(self,ISBN,Borrow):
        sql = DBcall.Mysql()
        return sql.checkOut(ISBN,Borrow)

    def addBook(self,ISBN):
        sql = DBcall.Mysql()
        temp = sql.checkBook(ISBN)
        admin = open("cache/admin.txt").read()
        if temp:
            file = open('logs/bookLog/' + ISBN + '.txt', 'a')
            info = sql.addcopy(ISBN)
            file.write("\n")
            file.write(str(datetime.datetime.now())[:-7] + '_' +"Book Copy "+info +" added by " + admin)
            file.close()
            return "Book Copy "+info +" added"

        else:
            file = open('logs/bookLog/' + ISBN + '.txt', 'w')
            info = sql.addbook(ISBN)
            p, lan, ti, au, isbn, y = info
            file.write(ISBN)
            file.write("\n")
            file.write(ti)
            file.write("\n")
            file.write(au[0])
            file.write("\n")
            file.write(p)
            file.write("\n")
            file.write(lan)
            file.write("\n")
            file.write(y)
            file.write("\n")
            file.write(str(datetime.datetime.now())[:-7] + '_' + 'Book Created by ' + admin)
            file.write("\n")
            file.write(str(datetime.datetime.now())[:-7] + '_' + 'Book Copy 001 added by ' + admin)
            file.close()
            return "Book " +ti+ " add into Library"

    def returnBook(self,ISBN,Borrow):
        sql = DBcall.Mysql()
        sql.returnBook(ISBN,Borrow)

    def pickUp(self,ISBN,Borrow):
        sql = DBcall.Mysql()
        sql.pickUp(ISBN,Borrow)

    def checkOut(self,ISBN,Borrow):
        sql = DBcall.Mysql()
        sql.checkOut(ISBN,Borrow)
