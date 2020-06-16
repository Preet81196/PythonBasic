import re

str1 = 'Preet_811'
str2 = 'Preet@811&'
str3 = 'PREET_ patel'

print(bool(re.match('^[A-za-z0-9_]*$',str1)))
print(bool(re.match('^[A-za-z0-9_]*$',str2)))
print(bool(re.match('^[A-za-z0-9_]*$',str3)))

