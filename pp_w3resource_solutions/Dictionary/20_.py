list_dict1 =[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
    {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

xx = set(val for dic in list_dict1 for val in dic.values())

print(xx)
