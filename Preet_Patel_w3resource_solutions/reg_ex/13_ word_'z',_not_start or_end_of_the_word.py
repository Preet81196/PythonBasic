import re

str1 = 'zpatelpatelz'
str2 = 'patelzpatel'

print(bool(re.search('\Bz\B',str1)))
print(bool(re.search('\Bz\B',str2)))

