import socket
import sys
import multiprocessing
import multiprocessing.connection as connection

#https://realpython.com/python-sockets/\
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
def create_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        i = 0
        s.connect((HOST, PORT))
       
        s.sendall(b"Hello, world")
        message_size = int(s.recv(1024))
        processes = s.recv(message_size)
        print(processes)
        

        
create_client()