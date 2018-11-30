import os,shutil,isbnlib,json,urllib,datetime,pymysql.cursors
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

    def addbook(self,ISBN):
        p,lan,ti,au,isbn,y = self.dump(ISBN)
        connection = self.con()
        try:
            with connection.cursor() as cursor:
                sqlQuery = "INSERT INTO book(ISBN13, Title, Author, Publisher, Language, Year, Count) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                sqlQuery2 = "INSERT INTO copy(ISBN13, Copy) VALUES (%s,%s)"
                cursor.execute(sqlQuery,(isbn,ti,au[0],p,lan,y,'0'))
                cursor.execute(sqlQuery2, (isbn, "001"))
                connection.commit()
        finally:
            connection.close()
        curl = isbnlib.cover(ISBN)['smallThumbnail']
        urllib.urlretrieve(curl,"repository/cover/"+ISBN+".jpg")
        return "new book add"

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
        return "new copy" + copy + ' add'

    def checkOut(self,ISBN,BorrrowID):
        if len(self.bookBorrow(BorrrowID)) >= 10:
            return "Check out failed! More than 10 books were borrowed by the reader already!"
        connection = self.con()
        a = "No book available"
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
                    cursor.execute(sqlQuery,(BorrrowID,str(now)[:-7],ISBN,result[0]['copy']))
                    cursor.execute(sqlQuery2,(ISBN))
                    cursor.execute(sqlQuery3,(BorrrowID,ISBN,result[0]['copy']))
                    connection.commit()
                    a = "Check out successed"
        finally:
            connection.close()
        return a

    def checkReserve(self,ISBN):
        #############################
        print "WIP"
        return False

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
                if not self.checkReserve(ISBN):
                    sqlQuery = "UPDATE copy SET BorrowID=NULL, ReturnDate=NULL WHERE ISBN13=%s AND Copy=%s"
                    sqlQuery2 = "DELETE FROM readerborrow WHERE ISBN13=%s AND Id=%s AND Copy =%s"
                    cursor.execute(sqlQuery,(ISBN,copy))
                    cursor.execute(sqlQuery2,(ISBN,BorrowID,copy))
                    connection.commit()
                else:
                    #############################
                    print "WIP"
        finally:
            connection.close()
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
        return True

a=Mysql()
#print a.checkOut("9780345476722","0980485")
#print a.checkOut("9781881133209","0980485")
print a.bookBorrow("0980485")