import os,DBcall,datetime
class MemberManagement:
    def addReader(self,name,add,phone):
        sql = DBcall.Mysql()
        id = sql.addReader(name,add,phone)
        admin = open("cache/admin.txt").read()
        file = open('logs/readerLog/'+id+'.txt','w')
        file.write(id)
        file.write("\n")
        file.write(name)
        file.write("\n")
        file.write(add)
        file.write("\n")
        file.write(phone)
        file.write("\n")
        file.write(str(datetime.datetime.now())[:-7] +'_'+'Reader Created by '+ admin )
        return id