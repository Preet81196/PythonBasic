items = input("enter data using comma : ")
word = [word for word in items.split(",")]
word.sort()
print(word)