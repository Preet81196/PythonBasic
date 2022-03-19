
from os import listdir
import re
from os.path import isfile, join
files_list = [f for f in listdir('c:/Users/BOBBY/Desktop/rename/Tuple') if isfile(join('c:/Users/BOBBY/Desktop/rename/Tuple', f))]
print(files_list);

for i in files_list:
    new_name = i.replace(' ','_')
                                # work pending
print(new_name)
