count = dict()
with open("preet.txt","r") as fh:
    words = fh.read().split()
    max_len = len(max(words, key=len))
    x= [word for word in words if len(word) == max_len]
print(x)
