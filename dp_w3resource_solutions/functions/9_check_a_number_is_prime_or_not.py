"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function that takes a number as a parameter and check the number is prime or not.
"""

# A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
# other than 1 and itself.


def is_prime(a):
    if not isinstance(a, int) and a <= 1:
        return -1
    for each in range(2, a):
        if a % each == 0:
            return False
    return True


print(is_prime(18))
