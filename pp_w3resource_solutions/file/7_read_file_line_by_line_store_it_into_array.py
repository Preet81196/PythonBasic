store_array = []
with open("preet.txt","r") as fh:
    lines = fh.readlines()
    store_array.append(lines)
print(store_array)

print(type(store_array))                #????? pending