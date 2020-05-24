"""str1 = "m"
if len(str1) >= 2:
    print(str1[0:2]+str1[-2:])
elif len(str1) < 2:
    print("string is empty")"""



#2
def name(str):
    if len(str) >= 2:
        return(str[0:2] + str[-2:])
    else:
        return ""
    
print(name("preetpatel"))