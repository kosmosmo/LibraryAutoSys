cache = "cache/readerid.txt"
curid = open(cache).read()
newid = str(int(curid)+1).zfill(7)
file = open(cache,"w")
file.write(newid)
file.close()
print newid