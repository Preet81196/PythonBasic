import re

str1 = 'pm.'
str2 = 'pm  '

print(bool(re.match('\S*$',str1)))
print(bool(re.match('\S*$',str2)))