import socket
import sys

#https://realpython.com/python-sockets/\
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
def create_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        i = 0
        s.connect((HOST, PORT))
       
        s.sendall(b"Hello, world")
        data = s.recv(30000)
        print(f"Received {data!r}")
       
        # while(i < 10):
        #     s.sendall(b"Hello, world")
        #     data = s.recv(30000)
        #     print(f"Received {data!r}")
        #     i = i+1
create_client()