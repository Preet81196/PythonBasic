import re


str1 = "preet811"
str2 = "preet"

print(bool(re.match('.*[0-9]$',str1)))
print(bool(re.match('.*[0-9]$',str2)))