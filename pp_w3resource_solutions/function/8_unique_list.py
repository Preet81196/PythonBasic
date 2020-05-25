def unique_list(list1):
    x =[]
    for i in list1:
            if i not in x:
                x.append(i)
    ssreturn x


print(unique_list([1,1,2,3,3,3,4,5]))
