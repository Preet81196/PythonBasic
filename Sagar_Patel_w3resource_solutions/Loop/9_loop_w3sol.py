"""  Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34"""

nterms = 50

n1,n2 = 0,1
while n1 < nterms:
        print(n1,end=" ")
        n1, n2 = n2, n1 + n2
