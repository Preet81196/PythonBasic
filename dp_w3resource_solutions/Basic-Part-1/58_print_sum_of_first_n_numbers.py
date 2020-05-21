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

# Other way
# answer = sum(range(n+1))
# print('Sum:', answer)
# print(timeit.timeit('sum(range(20))', number=1))  # 2.012999999967402e-06

# Upper and Lower code both are same, complexity is also same, running just a single loop and adds to a variable
# Although Sum function is built-in and pre-compiled so its a faster solution
# Otherwise, creating a list and then returning its elements sum employs 2 loops, (creating and finding sum)

# Another way
# def main():
#     answer = 0
#     for each in range(20):
#         answer += each
#     return answer
#
#
# print(timeit.timeit('main()', setup='from __main__ import main', number=1))  # 3.248000000011242e-06
