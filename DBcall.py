import os,shutil,isbnlib,json,urllib,datetime
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
