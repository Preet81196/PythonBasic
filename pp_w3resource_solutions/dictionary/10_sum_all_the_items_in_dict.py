d1 = {"number1":10,"number2":20,"number3":30,"number4":40,}
sum = 0
sum1 = 0

for i in d1:
        sum += d1[i]
print(sum)

for i in d1.values():               #2nd method
    sum1 = sum1 + i
print(sum1)
