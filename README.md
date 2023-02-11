Run Instructions

prereqs: python3, windows os

Please run on a windows os using the command prompt

Stage 1

print to console

python3 stage1.py

Options:

-f file_name.txt - Saves the process output to file_name.txt on the client machine

Stage 2

python3 stage2.py 

Options:

-f file_name.txt - Saves the process output to file_name.txt on the client machine

-hs hostIP - Sets the server IP 
-hc hostIP - Sets the client IP 

-ps port - Sets server port
-pc port - Sets client port

Will use localhost and a default port number of 12345 if not set

After entering the stage 2 command the current terminal will become the server and a new terminal that automatically opens will be the client

Stage 3

python3 stage3.py

Options:

-tf - targets file_name.txt from the server - REQUIRED

    -note if entering a relative path there is no need to put a \ as the first character

-f file_name.txt - Saves the target file to file_name.txt on the client machine

-hs hostIP - Sets the server IP 

-hc hostIP - Sets the client IP 

-ps port - Sets server port
-pc port - Sets client port

Will use localhost and a default port number of 12345 if not set

After entering the stage 3 command the current terminal will become the server and a new terminal that automatically opens will be the client



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