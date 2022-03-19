"""Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd'] """

data  = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
data = [t for t in data if t]
print(data)