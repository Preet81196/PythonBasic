"""3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dict1 = {1:10,2:10}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}


new_dict = {}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

print(new_dict)

"""no need to create new dictionary update key value pairs in dict1 """
print("srp modified")
dict1.update(dict2)
dict1.update(dict3)


print(dict1)
