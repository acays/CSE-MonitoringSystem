import socket
import sys
from Stage1 import *
#https://realpython.com/python-sockets/
    
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
def create_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
    
        while True:
            s.listen()
            conn, addr = s.accept()    
            with conn:
                print(f"Connected by {addr}")
                
                while True:
                    data = conn.recv(30000)
                    if not data:
                        break
                    # processes = get_processes()
                    # print("size is ", sys.getsizeof(processes))
                    
                    # print("data is ", data)
                    # conn.sendall(data)
                    conn.sendall(bytes(get_processes(), 'utf-8'))
                    # conn.sendall(get_processes(), 'utf-8')
    
create_server()