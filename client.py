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
                
        if isStage3 :
            server = create_server(host, port)
            send_message(server, str(isStage3))
            
            print(receive_directories(server))
            receive_file(server)
            
            server.close()
            
        
    except KeyboardInterrupt:
        server.close()
        pass
def receive_directories(server) :
    message_size = int(server.recv(1024))
    directories = server.recv(message_size)
    
    return directories
   
def create_server(host, port) :
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect to server on local computer
    server.connect((host,port))
    
    return server

def send_message(server, message) :  # message you send to servers
    server.send(message.encode('ascii'))
    

    
    
def receive_file(server) : 
    # Write File in binary
    file = open('client-file.txt', 'wb')

    num_lines = int(server.recv(1024))
    # line = server.recv(1024)
    line = "default"
        
    # https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-handling-file-conte
    for i in range(num_lines):
        line = server.recv(1024)
        # print("before")
        line = line[2:len(line)-1]
        line = str(line) + '\n'
        line = bytes(line, 'utf-8')
        file.write(line[2:len(line)])
        # print("after")
        # line = server.recv(1024)
        

    print('File has been received successfully.')
         
def receive_processes(server) :
    message_size = int(server.recv(1024))
    processes = server.recv(message_size)
    
    return processes
 
client(True)