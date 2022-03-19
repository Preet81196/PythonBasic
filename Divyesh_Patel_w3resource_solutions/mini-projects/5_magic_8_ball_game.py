"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 10/06/20
* @decription: Create a Python project of a Magic 8 Ball which is a toy used for behaviour-telling advice about friend.
"""

import random

with open('quotes.txt') as handle:
    quotes = handle.read().split('\n')


print("""
 __  __          _____ _____ _____    ___  
 |  \/  |   /\   / ____|_   _/ ____|  / _ \ 
 | \  / |  /  \ | |  __  | || |      | (_) |
 | |\/| | / /\ \| | |_ | | || |       > _ < 
 | |  | |/ ____ \ |__| |_| || |____  | (_) |
 |_|  |_/_/    \_\_____|_____\_____|  \___/ 
""")

print('Hello World, There is some tweak in this program, We will tell you about yourself here...')

name = input('Enter your name: ')

print('Hello', name)

should_ask = True

while should_ask:
    print('Enter name to get information about him/her, done/Done to exit...')
    friend = input('Enter: ')
    if friend.lower() == 'done':
        quit()
    print('Thinking...')
    rand_number = random.randint(0, len(quotes)-1)
    print(quotes[rand_number])
    choice = input('Do you have another question? [Y/N] ')
    if choice.lower() == 'n':
        print('Exiting...')
        should_ask = False
