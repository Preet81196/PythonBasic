import re
str1 = '811preet'
str2 = 'preet811'

print(bool(re.findall('^8',str1)))
print(bool(re.findall('^8',str2)))