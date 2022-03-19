def up_low(str1):
    d ={"U_CASE":0,"l_case":0}
    for i in str1:
        if i.isupper():
            d["U_CASE"] += 1
        elif i.islower():
            d["l_case"] += 1
        else:
            pass
    print("main string :",str1)
    print("this is upcase",d["U_CASE"])
    print("this is lowcase",d["l_case"])
print(up_low('The quick Brown Fox'))