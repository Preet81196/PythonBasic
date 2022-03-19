l1 = [1,2,3,4,(1,2),4,6]
count = 0
for i in l1:
    if isinstance(i, tuple):
        break
    count += 1

print(count)