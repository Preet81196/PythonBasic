"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 30/05/20
* @decription: TCP Client which sends data to server.py for getting capitalised words
"""

import socket


def main():
    host = '127.0.0.1'
    port = 5000

    sock = socket.socket()
    sock.connect((host, port))

    message = input('enter message: ')
    while message != 'done':
        sock.send(message.encode())
        data = sock.recv(1024).decode()
        print('received from server:', data)
        message = input('enter message: ')
    sock.close()


if __name__ == '__main__':
    main()
