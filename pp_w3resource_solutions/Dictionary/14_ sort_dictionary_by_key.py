dict1 = {4:1,2:2,1:3,3:4}

for k in sorted(dict1):
    print(k,dict1[k])
print()


[ print("by keys :",k, "---->" , v) for (k, v) in sorted(dict1.items()) ]           # by keys

print()

[ print("by values :",v, "---->" , k) for (k, v) in sorted(dict1.items()) ]           #by values