import sys
from process_list import * 

from server import *
from client import *

host_server = '127.0.0.1'
port_server = 12345

host_client = '127.0.0.1'
port_client = 12345
file_name = None
i = 1

while i < len(sys.argv) :
    if sys.argv[i] == "-f" :
        file_name = sys.argv[i+1]
    elif sys.argv[i] == "-hs" :
        host_server = sys.argv[i+1]
    elif sys.argv[i] == "-ps" :
        port_server = sys.argv[i+1]  
    elif sys.argv[i] == "-hc" :
        host_client = sys.argv[i+1]
    elif sys.argv[i] == "-pc" :
        port_client = sys.argv[i+1]
    
    i = i + 2
    

print("inputs are", file_name, host_server, port_server)


server(host_server, port_server)

