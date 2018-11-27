import os,DBcall
class ReaderManagement:
    def addRead(self,name,phone,add):
        json = DBcall.Json()
        json.addReader(name,phone,add)


a = ReaderManagement()
a.addRead("poop","123","shithole")