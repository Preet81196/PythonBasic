import re

str1 = "Exercises number 1, 12, 13,345 and 1221 are important"

x = re.findall(r'[0-9]{1,3}',str1)
print(x)