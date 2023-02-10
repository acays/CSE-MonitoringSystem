
import socket
import time
 
def client(isStage3):
    
    try: 
        port = 12345
        host = '127.0.0.1'
        
        while True and isStage3 == False:
            time.sleep(60)
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
    file = open('client-file.txt', 'w')

    num_lines = int(server.recv(1024))
    # line = server.recv(1024)
    line = "default"
    print()
    print("lines sent is", num_lines)
    send_message(server, "ready for next line") 
    
    for i in range(num_lines):
        line = server.recv(1024)
         
        line = process_line(line, i, num_lines)
        print()
        file.write(line + "\n")

        if i < num_lines-1 :
            send_message(server, "ready for next line")        

    print('File has been received successfully.')
    
def process_line(line, i, num_lines) :
    line = str(line)
    print("line is:", line)
    if i == num_lines-1 :
        line = line[4:len(line)-2]
    else :
         line = line[4:len(line)-8]
    print("line is:", line)
    # line = str(line) + '\n'
    return line
                
def receive_processes(server) :
    message_size = int(server.recv(1024))
    processes = server.recv(message_size)
    
    return processes
if __name__ == "__main__":
    client(False)