"""a= float(input("enter num 1:"))
b= float(input("enter num 2:"))
c= float(input("enter num 3:"))

if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c

    print("the larger is",largest)"""
""""
#using forloop(2)
largest_so_far= -1
print("before",largest_so_far)
for the_num in [9,41,12,3,74,15]:
   if the_num > largest_so_far:
    largest_so_far = the_num
    print(largest_so_far,the_num)
print("after",largest_so_far)
"""
"""
#counting in loops(3)
count =0
print("brfor",count)
for thing in [9, 41, 12, 3, 74, 15]:
    count=count+1
    print(count,thing)
print("after",count)
"""


"""#summing in loop (4)
sum = 0
print("brfor",count)
for thing in [9, 41, 12, 3, 74, 15]:
    sum = sum + thing
    print(sum,thing)
print("after",sum)"""


count = 0
sum = 0
print("before", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count+1
    sum = sum+value
print(count,sum,value)
print("after",count,sum,sum/count)