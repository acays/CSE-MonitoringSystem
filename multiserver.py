
# https://www.geeksforgeeks.org/socket-programming-multi-threading-python/


# import socket programming library
import socket
 
# import thread module
from _thread import *
import threading
from Stage1 import *
 
print_lock = threading.Lock()
 

def client_service(conn):
    while True:
 
        # data received from client
        data = conn.recv(1024)
        if not data:
            print('Bye')
             
            # lock released on exit
            print_lock.release()
            break

        processes = get_processes()
        # send back reversed string to client
        conn.sendall(bytes(str(sys.getsizeof(processes)), 'utf-8'))
        conn.sendall(bytes(str(processes), 'utf-8'))
 
    # connection closed
    conn.close()
 
 
def Main():
    host = ""
 
    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
 
        # establish connection with client
        c, addr = s.accept()
 
        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        # Start a new thread and return its identifier
        start_new_thread(client_service, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()