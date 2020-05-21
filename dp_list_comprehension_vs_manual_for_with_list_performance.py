"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 21/05/20
* @decription: Performance test between list comprehension and for loop for a list.
* @outcome: Both are same, both uses 1 for loop, assigns a formatted value to a list
"""

import timeit

# List comprehension
print(timeit.timeit("[x.replace('','_') for x in ['divyesh patel', 'hardik patel', 'preet patel', 'dhruvil dipeshji']]", number=1))
# 4.561000000014026e-06


# Splitting that List comprehension into 2 sub-parts
def main():
    final_list = list()
    for each in ['divyesh patel', 'hardik patel', 'preet patel', 'dhruvil dipeshji']:
        final_list.append(each.replace('', '_'))
    return final_list


print(timeit.timeit('main()', setup='from __main__ import main', number=1))
# 4.449000000017467e-06
