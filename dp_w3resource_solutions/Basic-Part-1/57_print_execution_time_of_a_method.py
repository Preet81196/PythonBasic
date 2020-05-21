"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 21/05/20
* @decription: Write a program to get execution time for a Python method.
"""
import timeit


def test():
    for each in range(100):
        pass


time_taken = timeit.timeit("test()", setup="from __main__ import test", number=1)
print('Time Elapsed:', time_taken)


