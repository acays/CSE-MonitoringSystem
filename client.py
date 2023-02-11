
import socket
import time
import sys
 
def client(isStage3, host, port, file_name):
    
    try: 
    
        # in stage 2
        while True and isStage3 == False:
            time.sleep(60)
            server_conn = create_server_conn(host, port)
            send_message(server_conn, str(isStage3))
            processes = receive_processes(server_conn)
            
            if file_name == None :
                print(processes)
            else :
                process_file = open(file_name, "w")
    
                process_file.write(processes() + "\n")
                
        if isStage3 :
            server_conn = create_server_conn(host, port)
            send_message(server_conn, str(isStage3))
            
            print(receive_directories(server_conn))
            receive_file(server_conn)
            
            server_conn.close()
            
        
    except KeyboardInterrupt:
        server_conn.close()
        pass
def receive_directories(server) :
    message_size = int(server.recv(1024))
    directories = server.recv(message_size)
    
    return directories
   
def create_server_conn(host, port) :
    server_conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect to server on local computer
    server_conn.connect((host,port))
    
    return server_conn

def send_message(server_conn, message) :  # message you send to servers
    server_conn.send(message.encode('ascii'))
    
def receive_processes(server) :
    message_size = int(server.recv(1024))
    processes = server.recv(message_size)
    
    return processes
        
def receive_file(server) : 
    file = open('client-file.txt', 'w')

    num_lines = int(server.recv(1024))
    # line = server.recv(1024)
    line = "default"
    send_message(server, "ready for next line") 
    
    for i in range(num_lines):
        line = server.recv(1024)
         
        line = process_line(line, i, num_lines)
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
                


if __name__ == "__main__":
    file_name = sys.argv[3]
    if sys.argv[3] == "None":
        file_name = None
    
    
    client(eval(sys.argv[4]), sys.argv[1], int(sys.argv[2]), file_name)
    