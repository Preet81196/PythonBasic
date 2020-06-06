"""Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. """


num = int(input("enter number: "))

dif = num - 17

if dif >= 17:
    print(dif*2)
else:
    print(" less than 17")
