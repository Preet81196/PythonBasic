"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
        in the form (x, x*x).
"""

# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = 5

adict = {each: each**2 for each in range(1, n+1)}
print(adict)
