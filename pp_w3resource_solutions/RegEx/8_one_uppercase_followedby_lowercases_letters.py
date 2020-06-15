import re
str1 = 'PREETPatel'
str2 = "preetpatel"

print(bool(re.search('[A-Z][a-z]+',str1)))
print(bool(re.search('[A-Z][a-z]+',str2)))