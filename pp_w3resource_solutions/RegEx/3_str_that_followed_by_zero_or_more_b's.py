import re
str = "ab ab c"
if re.search('[b]+',str):
    print("found a match")
else:
    print("not found")