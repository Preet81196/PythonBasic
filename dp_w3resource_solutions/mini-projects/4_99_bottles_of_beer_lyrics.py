"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 10/06/20
* @decription: Create a Python project that prints out every line of the song "99 bottles of beer on the wall."
"""

# Note: Try to use a built in function instead of manually type all the lines.


def display_lyrics():
    current_count = 99
    while current_count > 0:
        print("{} bottles of beer on the wall, {} bottles of beer.".format(current_count, current_count))
        current_count -= 1
        print("Take one down and pass it around, {} bottles of beer on the wall.".format(current_count))
        print()

    print('No more bottles of beer on the wall, no more bottles of beer.')
    print('Go to the store and buy some more, 99 bottles of beer on the wall.')


if __name__ == '__main__':
    display_lyrics()
