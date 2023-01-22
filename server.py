import socket
import sys
from Stage1 import *
#https://realpython.com/python-sockets/\
    
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
def create_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        
        while True:
            s.listen()
            conn, addr = s.accept()    
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    # conn.sendall(bytes(get_processes(), 'utf-8'))
                    conn.sendall(data, 'utf-8')

create_server()