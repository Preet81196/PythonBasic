"""
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""

given_function = input("Sample fucntion : ")

p_index = given_function.find("(")

if  not p_index >= 0:
    print("Please enter valid function along with empty parenthesis")
    exit()

function_name = given_function[0:p_index]

print("Expected Result : ")
print("Some extra details")
print(function_name.__doc__)