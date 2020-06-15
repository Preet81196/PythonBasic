import re
str = "abb bbb cb"
str1 = "ab ab"
print(bool(re.search('b{2,3}',str)))
print(bool(re.search('b{2,3}',str1)))