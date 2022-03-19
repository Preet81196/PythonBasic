str1 = "123456789"
result = ""

for i in (range(len(str1))):
        if i % 2 == 0:
            result = result + str1[i]
            print(result)
            
