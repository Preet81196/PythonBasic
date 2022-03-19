import json

python_obj ={
    "name":"preet",
    "age" : 23,
    "phone":8141117475
}
print(type(python_obj))
print("python_obj :",python_obj)

json_data = json.dumps(python_obj)
print()

print(type(json_data))
print("json_obj :",json_data)