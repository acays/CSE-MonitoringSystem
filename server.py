
# https://www.geeksforgeeks.org/socket-programming-multi-threading-python/


# import socket programming library
import socket
import subprocess
# import thread module
from _thread import *
import threading
from process_list import *
from pathlib import Path

import sys

print_lock = threading.Lock()
 

def client_service(conn, file_name):
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
            
            # checking to see if the full path is already given
            if file_name[0:3] == "C:'\'" :
                file_path = file_name
            # otherwise assume path starts from current directory
            else :      
                cur_dir = Path(Path.cwd())
                file_path = Path.joinpath(cur_dir, "\\" + file_name)
                
            print("file being sent is:", file_path)
            send_file(conn, file_name)
        else :
            send_processes(conn)
       
    conn.close()
    
def send_directories(conn) :
    directories = str(subprocess.check_output("dir", shell=True))
    conn.sendall(bytes(str(sys.getsizeof(directories)), 'utf-8'))
    conn.sendall(bytes(str(directories), 'utf-8'))
    
def send_processes(conn) :
    processes = get_processes()
    
    conn.sendall(bytes(str(sys.getsizeof(processes)), 'utf-8'))
    conn.sendall(bytes(str(processes), 'utf-8'))
    
def send_file(conn, file_name) :
    lines = read_lines(file_name)
    conn.send(bytes(str(len(lines)), 'utf-8'))

    for line in lines:
        client_go_ahead = conn.recv(1024)
        if client_go_ahead :
            conn.send(bytes(str(line), 'utf-8'))
    
    
    print('File has been transferred successfully.')

def read_lines(path) :
    file = open(path, 'rb')
    
    lines = file.readlines()
    
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        "Line{}: {}".format(count, line.strip())
        
    file.close()
        
    return lines
 
def server(host, port, file_name):
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

        start_new_thread(client_service, (conn, file_name))

 
if __name__ == "__main__":
    server('127.0.0.1', 12345, "output.txt")