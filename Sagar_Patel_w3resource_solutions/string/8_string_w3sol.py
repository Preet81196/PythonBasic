"""  Write a Python function that takes a list of words and returns the length of the longest one"""



def word(w1,w2,w3):
    if len(w1)> len(w2) and len(w3):
        return len(w1)
    elif len(w2) > len(w3) and len(w1):
        return len(w2)
    elif len(w3) > len(w2) and len(w1):
        return len(w3)
    quit()

print (word("sa","niks","srp"))

