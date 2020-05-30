"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 20/05/20
* @decription: Write a Python to find local IP addresses using Python's stdlib
"""

import socket

triple_host = socket.gethostbyname_ex(socket.gethostname())
ip_address_list = triple_host[2]
for each in ip_address_list:
    print(each)

