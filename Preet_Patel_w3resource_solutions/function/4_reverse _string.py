"""def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s                    #here i don't understand this method
print(reverse("preet"))"""

def reverse(str1):
    str1 = str1[::-1]
    return str1
str1 = input("enter string :")
print(reverse(str1))