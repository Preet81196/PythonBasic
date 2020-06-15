import re
str1 = "apple_b"
str2 = "apple"

print(bool(re.findall('[^a][b]$',str1)))
print(bool(re.findall('[^a][b]$',str2)))