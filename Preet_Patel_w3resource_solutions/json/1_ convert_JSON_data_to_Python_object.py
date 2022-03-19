import json

json_data = '{"name":"preet","age" : 23,"phone":8141117475}'

data = json.loads(json_data)
print("name :",data["name"])
print("age :",data["age"])
print("phone :",data["phone"])

