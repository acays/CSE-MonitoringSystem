# https://www.geeksforgeeks.org/socket-programming-multi-threading-python/


import socket
import time
 
def client(isStage3):
    
    try: 
        
        
        # Define the port on which you want to connect
        port = 12345
        # local host IP '127.0.0.1'
        host = '127.0.0.1'
        
        while True and isStage3 == False:
            
            
            time.sleep(2)
            server = create_server(host, port)
            send_message(server, str(isStage3))
            
           
            print(receive_processes(server))
        
            
            
            # close the connection
            # s.close()
        if isStage3 :
            print("in stage 3")
        
    except KeyboardInterrupt:
        server.close()
        pass
    
def create_server(host, port) :
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect to server on local computer
    server.connect((host,port))
    
    return server

def send_message(server, message) :  # message you send to server
    server.send(message.encode('ascii'))
    
    
def receive_file(server) : 
    # Write File in binary
    file = open('client-file.txt', 'wb')

    # Keep receiving data from the server
    line = server.recv(1024)

    while(line):
        file.write(line)
        line = server.recv(1024)

    print('File has been received successfully.')
         
def receive_processes(server) :
    
    # message received from server
    message_size = int(server.recv(1024))
    processes = server.recv(message_size)
    
    return processes
 
client(False)