"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 21/05/20
* @decription: Write a python program to find the sum of the first n positive integers.
"""
import timeit

n = int(input('Enter n: '))
answer = sum([each for each in range(n+1)])
print('Sum:', answer)
# print(timeit.timeit('sum([each for each in range(20)])', number=1))  # 4.500000000018378e-06


# Another way
# def main():
#     answer = 0
#     for each in range(20):
#         answer += each
#
#
# print(timeit.timeit('main()', setup='from __main__ import main', number=1))  # 3.248000000011242e-06
