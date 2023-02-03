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
            server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # connect to server on local computer
            server.connect((host,port))
        
           
            # message you send to server
            message = "send me the processes running on your machine"
            print(receive_processes(server, message))
        
            
            
            # close the connection
            # s.close()
        if isStage3 :
            print("in stage 3")
        
    except KeyboardInterrupt:
        server.close()
        pass
def receive_file(server) : 
    # Write File in binary
    file = open('client-file.txt', 'wb')

    # Keep receiving data from the server
    line = server.recv(1024)

    while(line):
        file.write(line)
        line = server.recv(1024)

    print('File has been received successfully.')
         
def receive_processes(server, message) :
     # message sent to server
    server.send(message.encode('ascii'))

    # message received from server
    message_size = int(server.recv(1024))
    processes = server.recv(message_size)
    
    return processes
 
client(False)