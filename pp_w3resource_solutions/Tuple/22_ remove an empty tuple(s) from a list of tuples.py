from typing import List, Union, Tuple

t1 = [(),(1),("preet"),(2),("divyesh"),()]
t1 = [i for i in t1 if i]
print(t1)


t1 = filter(None,t1)
print(t1)