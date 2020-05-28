def high1(list):
    max = None
    for i in list:
        if max is None :
            max = i 
        if max < i:
            max = i
    return max
print(high1([-1,-22,-8,-2.,0]))