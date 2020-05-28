def small1(list):
    small = None
    for i in list:
        if small is None :
            small = i 
        if small > i:
            small = i
    return small
print(small1([9,22,8,2,0]))