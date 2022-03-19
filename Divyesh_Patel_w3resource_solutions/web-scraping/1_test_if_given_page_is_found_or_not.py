"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 30/05/20
* @decription: Write a Python program to test if a given page is found or not on the server
"""

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = 'www.python.org'
port = 80

connection = sock.connect((target, port))
print(connection)
data_to_send = 'GET https://www.python.org'.encode()

connection.send(data_to_send)

