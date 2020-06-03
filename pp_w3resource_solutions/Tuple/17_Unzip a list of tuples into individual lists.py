t1 = [("preet",1),("divyesh",2),("sagar",3)]

unzip = [i for i,j in t1],[ j for i,j in t1]
print("1st method: ",unzip)

print()

#2nd
unzip1 = list(zip(*t1))
print("2nd method: ",unzip1)

#3rd
unzip3 = map(None, *t1)             #it is possile but here not working
print("3rd method: ",unzip3)