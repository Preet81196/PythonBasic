"""Write a Python program to remove duplicates from a list."""

list = [5,10,15,10]
final_list = []
for num in list:
    if num not in final_list:
        final_list.append(num)
print(final_list)


