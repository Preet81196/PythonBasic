"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 10/06/20
* @decription: Create a Python project to guess a number that has randomly selected.
"""

import random

guessed_number = random.randint(0, 100)
print('You can always input done/DONE to exit...')

while True:
    try:
        user_input = input("Enter Number: ")
        user_input = int(user_input)
    except:
        if user_input.lower() == 'done':
            print('EXITING...')
            quit()
        else:
            print('Invalid input, try again')
            continue

    if guessed_number is user_input:
        print('Great, You guessed it Right, Done')
        break
    elif guessed_number > user_input:
        print('Guess BIGGER...')
    else:
        print('Guess smaller...')

