"""Write a Python script to merge two Python dictionaries."""

dict1 = {1:10,2:10}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}

print("srp modified")
dict1.update(dict2)
dict1.update(dict3)
print(dict1)
