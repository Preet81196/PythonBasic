"""Write a Python program to multiply all the items in a dictionary."""

dict = {1:10,2:10}

res=1
for key in dict:
    res=res * dict[key]

print(res)