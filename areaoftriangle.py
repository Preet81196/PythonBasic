a= float(input("enter num 1:"))
b= float(input("enter num 2:"))
c= float(input("enter num 3:"))

s= (a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("the area of triengle {} ".format(area))