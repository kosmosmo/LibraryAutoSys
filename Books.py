import os,DBcall,datetime,json,collections,isbnlib
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

    def appendLog(self,path,content):
        file = open(path, 'a')
        for item in content:
            file.write("\n")
            file.write(str(datetime.datetime.now())[:-7] +'_'+item)
        file.close()

    def convertToTuple(self,dict):
        res = []
        for key,value in dict.items():
            res.append((int(value),key))
        return res

    def topBook(self,ISBN,count):
        dir = "cache/topBooks.txt"
        file = open(dir, 'r')
        data = json.load(file)
        file.close()
        if ISBN in data:
            data[ISBN] = count
        else:data[ISBN] = count
        tens = self.convertToTuple(data)
        tens = sorted(tens)
        while len(tens) > 10:
            tens.pop(0)
        dic = collections.defaultdict(int)
        for item in tens:
            dic[item[1]] = int(item[0])
        r = json.dumps(dic)
        file = open(dir,'w')
        file.write(r)
        file.close()

    def topReader(self,ID,count):
        dir = "cache/topBorrowers.txt"
        file = open(dir, 'r')
        data = json.load(file)
        file.close()
        if ID in data:
            data[ID] = count
        else:data[ID] = count
        tens = self.convertToTuple(data)
        tens = sorted(tens)
        while len(tens) > 10:
            tens.pop(0)
        dic = collections.defaultdict(int)
        for item in tens:
            dic[item[1]] = int(item[0])
        r = json.dumps(dic)
        file = open(dir,'w')
        file.write(r)
        file.close()





