import os,shutil,isbnlib,json,urllib,datetime,pymysql.cursors,Books
class Json:
    def tod(self,strr):
        strr = strr.split(' ')
        temp = ' '.join(strr[0].split('-') + strr[1].split(':'))
        return datetime.datetime.strptime(temp, '%Y %m %d %H %M %S')

    def dump(self,ISBN):
        info = []
        for key,value in isbnlib.meta(ISBN).items():
            info.append(value)
        return info

    def changepw(self,user,newpw):
        dir = "repository/admin/adminAcc.txt"
        with open(dir, 'r+') as f:
            data = json.load(f)
            data[user] = newpw
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

    def getpw(self,user):
        dir = "repository/admin/adminAcc.txt"
        with open(dir, 'r+') as f:
            data = json.load(f)
            if user not in data: return None
            else:return data[user]

    def addReader(self,name,add,phone):
        dir = "repository/reader/"
        ids = sorted(os.listdir(dir))
        newid = int(ids[-1][:-4])+1
        shutil.copy(dir+'0000000.txt', dir + str(newid).zfill(7) +'.txt')
        with open(dir + str(newid).zfill(7)  +'.txt', 'r+') as f:
            data = json.load(f)
            data["id"] = str(newid).zfill(7)
            data["name"] = name
            data["add"] = add
            data["phone"] = phone
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

    def createAdmin(self,user,pw):
        dir = "repository/admin/adminAcc.txt"
        with open(dir, 'r+') as f:
            data = json.load(f)
            if user in data:
                return False
            else:
                data[user] = pw
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        return True

    def addbook(self,ISBN):
        dir = "repository/book/" + ISBN
        os.makedirs(dir)
        shutil.copy('temp.txt', dir + '/000.txt')
        info = self.dump(ISBN)
        with open(dir + '/000.txt', 'r+') as f:
            data = json.load(f)
            data["Publisher"] = info[0]
            data["Language"] = info[1]
            data["Title"] = info[2]
            data["Authors"] = info[3]
            data["ISBN-13"] = info[4]
            data["Year"] = info[5]
            data["Copy"] = 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        shutil.copy(dir + '/000.txt', dir + '/001.txt')
        curl = isbnlib.cover("9780345476722")['smallThumbnail']
        urllib.urlretrieve(curl,"repository/cover/"+ISBN+".jpg")

    def addcopy(self,ISBN):
        dir = "repository/book/"+ISBN
        copys = os.listdir(dir)
        copys.sort()
        num = str(int(copys[-1][:-4])+1).zfill(3)
        shutil.copy(dir + '/000.txt', dir+'/' + num +'.txt')
        with open(dir +'/'+ num +'.txt', 'r+') as f:
            data = json.load(f)
            data["Copy"] = int(num)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        return True

    def checkOut(self,ISBN,Borrow):
        now = datetime.datetime.now()
        now.replace(second=int(now.second))
        now = now + datetime.timedelta(days=20)
        dir = "repository/book/" + ISBN + '/'
        copys = os.listdir(dir)
        for copy in copys:
            if copy != '000.txt':
                with open(dir + copy, 'r+') as f:
                    data = json.load(f)
                    if data['Borrowby'] == '':
                        data['Borrowby'] = Borrow
                        data['Returndate'] = str(now)[:-7]
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()
                        return True
        return False

    def returnBook(self,ISBN,Borrow):
        dir = "repository/book/" + ISBN+'/'
        copys =os.listdir(dir)
        res = [None,None]
        for copy in copys:
            with open(dir + copy, 'r+') as f:
                data = json.load(f)
                if data['Borrowby'] == Borrow:
                    if not res[0]:
                        res[0] = copy
                        res[1] = data['Returndate']
                    elif data['Returndate'] > res[1]:
                        res[0] = copy
                        res[1] = data['Returndate']
        if res[0] != None:
            with open(dir + res[0], 'r+') as f:
                data = json.load(f)
                data["Borrowby"] = ""
                data["Returndate"] = ""
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

    def reserve(self,ISBN,Borrow):
        return


class Mysql:
    def retriveBook(self,ISBN):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Title, Author, Publisher,Language, Year FROM book WHERE ISBN13=%s"
                cursor.execute(sqlQuery, (ISBN))
                result = cursor.fetchone()
        finally:
            connection.close()
        print result
        return [result["Publisher"],result["Language"],result["Title"],result["Author"],ISBN,result["Year"]]

    def tod(self,strr):
        strr = strr.split(' ')
        temp = ' '.join(strr[0].split('-') + strr[1].split(':'))
        return datetime.datetime.strptime(temp, '%Y %m %d %H %M %S')

    def readerIn(self,BorrowID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Id FROM reader WHERE Id=%s"
                cursor.execute(sqlQuery,(BorrowID))
                result = cursor.fetchone()
        finally:
            connection.close()
        return result != None

    def getAllReader(self):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Id, Name FROM reader"
                cursor.execute(sqlQuery)
                result = cursor.fetchall()
                res = []
                for item in result:
                    res.append(item['Id']+'_'+item['Name'])
        finally:
            connection.close()
        return res

    def checkBook(self,ISBN):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13 FROM book WHERE ISBN13= %s"
                cursor.execute(sqlQuery, (ISBN))
                result = cursor.fetchone()
        finally:
            connection.close()
        return result != None


    def con(self):
        return pymysql.connect(host = 'localhost',
                                     user = 'root',
                                     port = 3306,
                                     password = '',
                                     db = 'library',
                                     cursorclass= pymysql.cursors.DictCursor)
    def dump(self,ISBN):
        info = []
        for key,value in isbnlib.meta(ISBN).items():
            info.append(value)
        return info

    def addbook(self,dump):
        p,lan,ti,au,isbn,y = dump
        if p == "":p = ti
        if au == "": au = ti
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "INSERT INTO book(ISBN13, Title, Author, Publisher, Language, Year, Count) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                sqlQuery2 = "INSERT INTO copy(ISBN13, Copy) VALUES (%s,%s)"
                sqlQuery3 = "INSERT INTO author(ISBN13, Author) VALUES (%s, %s)"
                cursor.execute(sqlQuery,(isbn,ti,au[0],p,lan,y,'0'))
                cursor.execute(sqlQuery2, (isbn, "001"))
                cursor.execute(sqlQuery3,(isbn, au[0]))
                connection.commit()
        finally:
            connection.close()
        return

    def addcopy(self,ISBN):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT copy FROM copy WHERE ISBN13= %s"
                cursor.execute(sqlQuery, (ISBN))
                result = cursor.fetchall()
                res = []
                for item in result:
                    res.append(item["copy"])
                res.sort()
                copy = str(int(res[-1])+1).zfill(3)
                sqlQuery2 = "INSERT INTO copy(ISBN13, Copy) VALUES (%s,%s)"
                cursor.execute(sqlQuery2, (ISBN, copy))
                connection.commit()
        finally:
            connection.close()
        return copy

    def checkOut(self,ISBN,BorrrowID):
        if len(self.bookBorrow(BorrrowID)) >= 10:
            return "Check out failed! More than 10 books were borrowed by the reader already!"
        connection = self.con()
        a = False
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT copy FROM copy WHERE ISBN13=%s AND BorrowID IS NULL"
                cursor.execute(sqlQuery,(ISBN))
                result = cursor.fetchall()
                if result:
                    now = datetime.datetime.now()
                    now.replace(second=int(now.second))
                    now = now + datetime.timedelta(days=20)
                    sqlQuery = "UPDATE copy SET BorrowID=%s, ReturnDate=%s WHERE ISBN13=%s AND Copy=%s"
                    sqlQuery2 = "UPDATE book SET Count=Count+1 WHERE ISBN13=%s"
                    sqlQuery3 = "INSERT INTO readerborrow(Id,ISBN13,Copy) VALUES (%s,%s,%s)"
                    sqlQuery4 = "SELECT Count FROM book WHERE ISBN13=%s"
                    sqlQuery5 = "SELECT Count FROM reader WHERE Id=%s"
                    cursor.execute(sqlQuery,(BorrrowID,str(now)[:-7],ISBN,result[0]['copy']))
                    cursor.execute(sqlQuery2,(ISBN))
                    cursor.execute(sqlQuery3,(BorrrowID,ISBN,result[0]['copy']))
                    cursor.execute(sqlQuery4,(ISBN))
                    count = cursor.fetchone()["Count"]
                    connection.commit()
                    cursor.execute(sqlQuery5, (BorrrowID))
                    reader = cursor.fetchone()["Count"]
                    connection.commit()
                    a = True
                    self.borrowCount(BorrrowID)
                    bk = Books.BookManagement()
                    bk.topBook(ISBN,count)
                    bk.topReader(BorrrowID,reader)
        finally:
            connection.close()
        return a

    def checkHold(self,ISBN,BorrowID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Reid FROM readerreserve WHERE ISBN13=%s AND Id=%s AND Inhold=%s"
                cursor.execute(sqlQuery,(ISBN,BorrowID,'1'))
                result = cursor.fetchall()
        finally:
            connection.close()
        if len(result) == 0: return False
        return result[0]["Reid"]


    def pickUp(self,ISBN,BorrowID):
        temp = self.checkHold(ISBN,BorrowID)
        if not temp: return "Pick up not ready"
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Copy FROM copy WHERE ISBN13=%s AND ReturnDate=%s"
                cursor.execute(sqlQuery,(ISBN,'HOLD'))
                result = cursor.fetchone()
                if len(result) == 0:
                    self.checkOut(ISBN,BorrowID)
                else:
                    sqlQuery = "DELETE FROM readerreserve WHERE ISBN13=%s AND Id=%s AND Reid =%s"
                    sqlQuery2 = "UPDATE copy SET BorrowID=NULL, ReturnDate=NULL WHERE ISBN13=%s AND ReturnDate=%s"
                    cursor.execute(sqlQuery,(ISBN,BorrowID,temp))
                    cursor.execute(sqlQuery2,(ISBN,'HOLD'))
                    connection.commit()
                    self.checkOut(ISBN,BorrowID)
        finally:
            connection.close()
        return "Picked!"

    def checkReserve(self,ISBN):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Reid FROM readerreserve WHERE ISBN13=%s AND Inhold=0"
                cursor.execute(sqlQuery,(ISBN))
                result = cursor.fetchall()
        finally:
            connection.close()
        if len(result)== 0: return False
        else:return result[0]["Reid"]

    def returnBook(self,ISBN,BorrowID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ReturnDate FROM copy WHERE ISBN13=%s AND BorrowID=%s"
                cursor.execute(sqlQuery, (ISBN,BorrowID))
                result = cursor.fetchall()
                res = []
                for item in result:
                    res.append(item["ReturnDate"])
                date = sorted(res)[-1]
                sqlQuery = "SELECT Copy FROM copy WHERE ISBN13=%s AND BorrowID=%s AND ReturnDate=%s"
                cursor.execute(sqlQuery, (ISBN, BorrowID,date))
                result = cursor.fetchone()
                copy = result['Copy']
                temp = self.checkReserve(ISBN)
                fine = self.computeFine(ISBN,BorrowID)
                sqlQuery = "UPDATE reader SET Balance=Balance+%s  WHERE Id=%s"
                cursor.execute(sqlQuery, (fine,BorrowID))
                if not temp:
                    sqlQuery = "UPDATE copy SET BorrowID=NULL, ReturnDate=NULL WHERE ISBN13=%s AND Copy=%s"
                    cursor.execute(sqlQuery,(ISBN,copy))
                else:
                    sqlQuery = "UPDATE copy SET BorrowID=%s, ReturnDate=%s WHERE ISBN13=%s AND Copy=%s"
                    sqlQuery2 = "UPDATE readerreserve SET Inhold=%s WHERE ISBN13=%s AND Reid=%s"
                    cursor.execute(sqlQuery, ('HOLD','HOLD',ISBN, copy))
                    cursor.execute(sqlQuery2, ('1',ISBN,temp))
                    print "WIP"
                sqlQuery3 = "DELETE FROM readerborrow WHERE ISBN13=%s AND Id=%s AND Copy =%s"
                cursor.execute(sqlQuery3, (ISBN, BorrowID, copy))
                connection.commit()
        finally:
            connection.close()

    def bookReserve(self,BorrowID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13 FROM readerreserve WHERE ISBN13=%s"
                cursor.execute(sqlQuery, (BorrowID))
                result = cursor.fetchall()
        finally:
            connection.close()
        return result

    def bookBorrow(self,BorrowID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13 FROM readerborrow WHERE Id=%s"
                cursor.execute(sqlQuery, (BorrowID))
                result = cursor.fetchall()
        finally:
            connection.close()
        return result

    def makeReserve(self,ISBN,BorrowID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                Reid = str(datetime.datetime.now())[:-7]
                sqlQuery = "INSERT INTO readerreserve(ISBN13,Id,Reid) VALUES (%s,%s,%s)"
                cursor.execute(sqlQuery,(ISBN,BorrowID,Reid))
                connection.commit()
        finally:
            connection.close()
        return True

    def checkReserveAvi(self,ISBN):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13 FROM copy WHERE ISBN13=%s AND ReturnDate is NULL"
                cursor.execute(sqlQuery,(ISBN))
                result = cursor.fetchone()
        finally:
            connection.close()
        return result != None

    def addReader(self,name,add,phone):
        cache = "cache/readerid.txt"
        curid = open(cache).read()
        newid = str(int(curid) + 1).zfill(7)
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "INSERT INTO reader(Id,Name,Address,Phone) VALUES (%s, %s, %s, %s)"
                cursor.execute(sqlQuery,(newid,name,add,phone))
                connection.commit()
        finally:
            connection.close()
        file = open(cache, "w")
        file.write(newid)
        file.close()
        return newid

    def borrowCount(self,BorrowID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "UPDATE reader SET Count=Count+1 WHERE Id=%s"
                cursor.execute(sqlQuery,(BorrowID))
                connection.commit()
        finally:
            connection.close()

    def getBookTile(self,ISBN):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Title FROM book WHERE ISBN13=%s"
                cursor.execute(sqlQuery,(ISBN))
                result = cursor.fetchone()
        finally:
            connection.close()
        return result['Title']

    def getAllBook(self):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13, Title, Author FROM book"
                cursor.execute(sqlQuery)
                result = cursor.fetchall()
                res = []
                for item in result:
                    res.append(item['ISBN13']+'_'+item['Title']+'_'+item['Author'])
        finally:
            connection.close()
        return res

    def getBookAvi(self,ISBN):
        connection = self.con()
        res = [None,None]
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13, ReturnDate FROM copy WHERE ISBN13=%s"
                cursor.execute(sqlQuery,(ISBN))
                copys = cursor.fetchall()
                sqlQuery2 = "SELECT ISBN13 FROM copy WHERE ISBN13=%s AND ReturnDate is NULL"
                cursor.execute(sqlQuery2,(ISBN))
                avi = cursor.fetchall()
        finally:
            connection.close()
        res[0] = avi
        res[1] = copys
        return res

    def getBorrowed(self,ID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13 FROM readerborrow WHERE Id=%s"
                cursor.execute(sqlQuery,(ID))
                res = cursor.fetchall()
                isbns = []
                for item in res:
                    isbns.append(item["ISBN13"])
        finally:
            connection.close()
        return isbns

    def getReserved(self,ID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13 FROM readerreserve WHERE Id=%s"
                cursor.execute(sqlQuery,(ID))
                res = cursor.fetchall()
                isbns = []
                for item in res:
                    isbns.append(item["ISBN13"])
        finally:
            connection.close()
        return isbns

    def getReserveInfo(self,ID):
        connection = self.con()
        res = [None,None]
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ISBN13 FROM readerreserve WHERE Id=%s AND inhold=1"
                cursor.execute(sqlQuery, (ID))
                resss = cursor.fetchall()
                ready = []
                for item in resss:
                    ready.append(item["ISBN13"])
                sqlQuery = "SELECT ISBN13 FROM readerreserve WHERE Id=%s AND inhold=0"
                cursor.execute(sqlQuery, (ID))
                resss = cursor.fetchall()
                notready = []
                for item in resss:
                    notready.append(item["ISBN13"])
        finally:
            connection.close()
        res[0] = ready
        res[1] = notready
        return res

    def computeFine(self,ISBN,ID):
        now = datetime.datetime.now()
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT ReturnDate FROM copy WHERE ISBN13=%s AND BorrowId=%s AND ReturnDate IS NOT NULL"
                cursor.execute(sqlQuery, (ISBN,ID))
                res = cursor.fetchall()
                date = []
                for item in res:
                    date.append(item["ReturnDate"])
                date.sort()
                if date:
                    redated = date[-1]
                    ans = int((now - self.tod(redated)).days) * 20
                else:
                    ans = 0
        finally:
            connection.close()
        if ans <=0: return 0
        return ans

    def avgFine(self):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Balance FROM reader"
                cursor.execute(sqlQuery)
                res = cursor.fetchall()
        finally:
            connection.close()
        fines = []
        for item in res:
            fines.append(item["Balance"])
        return float(sum(fines))/len(fines)

    def retriveAdd(self,branch):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT address FROM branch WHERE branch=%s"
                cursor.execute(sqlQuery,(branch))
                res = cursor.fetchone()
        finally:
            connection.close()
        return res["address"]

    def getBranch(self):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT branch FROM branch"
                cursor.execute(sqlQuery)
                res = cursor.fetchall()
                ans = []

                for item in res:
                    ans.append(item["branch"])
        finally:
            connection.close()
        return ans

    def getReaderName(self,ID):
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "SELECT Name FROM reader WHERE Id=%s"
                cursor.execute(sqlQuery,(ID))
                result = cursor.fetchone()
        finally:
            connection.close()
        return result['Name']