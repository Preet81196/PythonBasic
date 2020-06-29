"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 29/06/20
* @decription: Write a Python program to create a backup of a SQLite database
"""

import sqlite3


def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')


con = sqlite3.connect('testing.sqlite')
bck = sqlite3.connect('backup.db')
with bck:
    con.backup(bck, pages=1, progress=progress)
bck.close()
con.close()
