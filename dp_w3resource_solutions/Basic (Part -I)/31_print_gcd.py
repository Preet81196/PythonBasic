"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 08:23:54
 * @modify date 19-05-2020 08:23:54
 * @desc Write a Python program to compute the greatest common divisor (GCD) of two positive integers
"""

try:
    inp_one = abs(int(input('Enter First: ')))
    inp_two = abs(int(input('Enter Second: ')))
except:
    print('invalid input, exiting')
    quit()

gcd_found = False

if inp_one % inp_two == 0 or inp_two % inp_one == 0:
    gcd = min(inp_one, inp_two)
    gcd_found = True

if not gcd_found:
    gcd = 1
    limit = min(inp_one, inp_two)

    for each in range(1, limit+1):
        if inp_one % each == 0 and inp_two % each == 0:
            gcd = each

print('GCD:', gcd)

# **************************************

# def get_gcd(inp_one, inp_two):
#     gcd = 1
#     if inp_one % inp_two == 0 or inp_two % inp_one == 0:
#         return min(inp_one, inp_two)
    
#     limit = min(inp_one, inp_two)

#     for each in range(1, limit+1):
#         if inp_one % each == 0 and inp_two % each == 0:
#             gcd = each
    
#     return gcd

# print(get_gcd(10, 40))