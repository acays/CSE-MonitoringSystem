Run Instructions

prereqs: python3, windows os

Please run on a windows os using the command prompt

Stage 1

print to console

python3 stage1.py

log to file (optional)

python3 stage1.py -f file_name.txt

Stage 2

python3 stage2.py 

Options:

-f file_name.txt - Saves the process output to file_name.txt on the client machine

-hs hostIP - Sets the server IP 

-hc hostIP - Sets the client IP 

-ps port - Sets server port
-pc port - Sets client port

Will use localhost and a default port number of 12345 if not set

After entering the stage2 command the current terminal will become the server and a new terminal that automatically opens will be the client

TODO

stage 1

-add linux functionality

stage 2

-user defined timing

-add linux functionality

stage 3

-configure directories

-can pass in target path

-add linux functionality