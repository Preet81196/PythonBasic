"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 20-05-2020 07:24:36
 * @modify date 20-05-2020 07:24:36
 * @desc Write a Python program to compute the future value of a specified principal amount, 
        rate of interest, and a number of years.
"""


def calculate_compounded_interest(principal, rate, years, times_per_year=1):
    return round(principal * ((1 + (rate/100)/times_per_year) ** (years * times_per_year)), 2)


print(calculate_compounded_interest(10000, 3.5, 7))