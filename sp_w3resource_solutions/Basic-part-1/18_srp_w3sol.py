"""Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. """


n1 = int(input("number 1:"))
n2 = int(input("number 2:"))
n3 = int(input("number 3:"))

res = n1+n2+n3

if n1==n2==n3 :
    print((res)*3)
else:
    print(res)
