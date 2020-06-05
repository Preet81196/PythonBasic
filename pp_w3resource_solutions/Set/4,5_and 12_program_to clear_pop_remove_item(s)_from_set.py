s = {"preet","divlo","sagar"}
s.pop()                                         #using pop() we can delete last element form set
print(s)

s1 = {"preet","divlo","sagar"}
s1.remove("divlo")
s1.discard("sagar")
print(s1)                                       #The remove() method removes the specified element from the set



s.clear()
s1.clear()                                      #Remove all elements
print("set no 1: ",s)
print("sen n 2: ",s1)

