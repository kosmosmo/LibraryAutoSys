import DBcall
class Authentication(object):
    def checkpw(self,user,password):
        json = DBcall.Json()
        return password == json.getpw(user)

    def createAdmin(self,user,password):
        json = DBcall.Json()
        return json.createAdmin(user,password)

    def changePW(self,user,oldpw,newpw):
        json = DBcall.Json()
        if oldpw == json.getpw(user):
            json.changepw(user,newpw)
            return True
        return False



