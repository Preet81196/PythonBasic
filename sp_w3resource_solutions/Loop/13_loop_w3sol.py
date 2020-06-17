"""    Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers
that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010"""
value = []
items=[x for x in input().split(',')]
for p in items:
    print (p)
    intp = int(p, 2)
    print (intp)
    if not intp%5:
        value.append(p)

print (','.join(value))