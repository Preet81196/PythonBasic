fh = open("preet1.txt","a")
fh.write("my name is preet")
fh.close()

fh = open("preet1.txt","r")
print(fh.read())