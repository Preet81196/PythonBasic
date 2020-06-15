import  re
str1 = 'preetpatel811'
str2 = '&&#$&@'
print(bool(re.match(r'^[0-9a-zA-Z]+', str1)))
print(bool(re.match('^[0-9a-zA-Z]+', str2)))