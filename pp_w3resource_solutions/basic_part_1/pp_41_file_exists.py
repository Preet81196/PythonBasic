"""file_name = input("enter file name :")
 
open("file_name","w")
print(file_name)"""

import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))