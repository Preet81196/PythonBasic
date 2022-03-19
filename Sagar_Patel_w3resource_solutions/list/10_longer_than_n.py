"""  Write a Python program to find the list of words that are longer than n from a given list of words."""
txt = input("enter")
n = int(input("enter n"))
w_len = []
txt1 = txt.split(" ")
for x in txt1:
    if len(x) > n:
        w_len.append(x)
print(w_len)


