import re
str1 = "The_apple"
str2 = "Apple"

print(bool(re.search(['^The',str1])))
print(bool(re.search(['^The',str2])))