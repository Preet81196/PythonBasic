import re
str1 = "preetpatel_bobby"
str2 = "PREETpate bobby"

print(bool(re.search('[a-z]+_[a-z]+',str1)))
print(bool(re.search('[a-z]+_[a-z]+',str2)))
