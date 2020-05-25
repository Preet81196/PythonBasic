def max(x,y,z):
    if(x > y) and (x > z) :
        return x 
    elif(y > z) and (y > x):
        return y
    elif(z > x) and (z > y):
        return z        

print(max(9,15,5))
