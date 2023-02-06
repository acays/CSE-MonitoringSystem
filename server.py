
# https://www.geeksforgeeks.org/socket-programming-multi-threading-python/


# import socket programming library
import socket
import subprocess
# import thread module
from _thread import *
import threading
from process_list import *
import os
from pathlib import Path

print_lock = threading.Lock()
 

def client_service(conn, isStage3):
    while True:
 
        # data received from client
        isStage3 = conn.recv(1024)
        if not isStage3:
            print('Bye')
             
            # lock released on exit
            print_lock.release()
            break

    
        if eval(isStage3) :
           
            send_directories(conn)
            cur_dir = Path(Path.cwd())
            file_dir = Path.joinpath(cur_dir, "test")
            file_path = Path.joinpath(file_dir, "test.txt")
            
            print("file being sent is:", file_path)
             # send_file(conn)
        else :
            send_processes(conn)
            
    # connection closed
    conn.close()
    
def send_directories(conn) :
    directories = str(subprocess.check_output("dir", shell=True))
    print("dir is  ", directories)
    conn.sendall(bytes(str(sys.getsizeof(directories)), 'utf-8'))
    conn.sendall(bytes(str(directories), 'utf-8'))
    
def send_processes(conn) :
    processes = get_processes()
    
    conn.sendall(bytes(str(sys.getsizeof(processes)), 'utf-8'))
    conn.sendall(bytes(str(processes), 'utf-8'))
    
def send_file(conn) :
    # Read File in binary
    file = open('test/test.txt', 'rb')
    # file = open(os.path.join('/test', "test.txt"))
    line = file.read(1024)
    
    # Keep sending data to the client
    while(line):
        conn.send(line)
        print("sent line:", line)
        line = file.read(1024)
    
    file.close()
    print('File has been transferred successfully.')

 
def server():
    host = ""
 
    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    server.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        conn, addr = server.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(client_service, (conn, False))
    server.close()

 

server()