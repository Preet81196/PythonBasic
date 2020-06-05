s1 = {1,2,3}
s2 = {1,2,4,5,6}
s3 = {1}

x = s1.symmetric_difference(s2)                     #contains all items from both set,
                                                    # but not the items that are present in both sets
print(x)