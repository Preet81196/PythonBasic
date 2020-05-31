"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 30/05/20
* @decription: acts as an TCP Server, Listens for requests and serves capital text
"""

import socket


def main():
    host = '127.0.0.1'  # This machine
    port = 5000

    sock = socket.socket()
    sock.bind((host, port))

    sock.listen(1)  # One connection at a time
    cl, addr = sock.accept()
    print('Connection from:', str(addr))
    while True:
        data = cl.recv(1024).decode()  # default UTF-8
        if not data:
            break
        print('From connected user:', data)
        data = data.upper()
        print('Sending this data:', data)
        cl.send(data.encode())  # default UTF-8
    cl.close()


if __name__ == '__main__':
    main()
