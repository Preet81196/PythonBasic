def even_num(list):
    num = []
    for i in list:
        if i % 2 == 0:
           num.append(i)
    return num
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
