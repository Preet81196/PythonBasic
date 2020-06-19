"""Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
Click me to see the sample solution"""





def poor(string):
    fnot = string.find('not')
    fpoor = string.find('poor')


    if fpoor > fnot and fnot>0 and fpoor>0:
        string = string.replace(string[fnot:(fpoor+4)], 'good')
        return( string)
    else:
        return (string)
        
print(poor('The lyrics is not that poor!'))
print(poor('The lyrics is poor!'))

