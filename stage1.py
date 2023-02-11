import sys
from process_list import * 


num_args = len(sys.argv)
    

if num_args == 3 and sys.argv[1] == "-f":
    save_processes_to_file(sys.argv[2])
else :
    print(get_processes())
    
    

    

