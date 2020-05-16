""""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
"""

try:
    number_one = int(input("Enter Number 1: "))
    number_two = int(input("Enter Number 2: "))
    number_three = int(input("Enter Number 3: "))
    answer = number_one + number_two + number_three

    if number_one == number_two == number_three:
        print(answer * 3)
    else:
        print(answer)

except:
    print("Invalid inputs, Exiting")
