"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Performance test between lists as queues vs. Collection's deques as queues
"""

import timeit

# Related docs can be found here https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
# Setup
# as per the article, If one wants to use lists are queues (First-In, First-Out), we can do it by alist.pop(0)
# using which we can pop out the first element
# But as per the docs this process if quiet slow, it needs to shift every elements
# But when we use, Collection's deque
# It's much faster, we can see here. We have iterated over 100000 elements of list for 10 times to get an average
# popping on list, we can see it takes around 200X slow than Collection's deque's popleft method


list_queue_pop_setup = 'len_alist=100000;alist=list(range(100000))'
dq_pop_setup = 'len_alist=100000;from collections import deque;dq=deque(list(range(100000)))'

print(timeit.timeit('while len_alist > 0: alist.pop(0);len_alist-=1', setup=list_queue_pop_setup, number=10))
print(timeit.timeit('while len_alist > 0: dq.popleft();len_alist-=1', setup=dq_pop_setup, number=10))
