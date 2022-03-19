import re

pattern = ['fox']
text = 'The quick brown fox jumps over the lazy dog.'

match = re.search('fox',text)

starting = match.start()
ending = match.end()

print("the 'fox' is staring from {} and ending with {}".format(starting,ending))