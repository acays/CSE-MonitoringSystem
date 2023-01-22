
import os
import sys

#https://www.geeksforgeeks.org/python-get-list-of-running-processes/
def get_processes():
    # Running the aforementioned command and saving its output
    processes = os.popen('wmic process get description, processid').read()
    
    
    
    # Displaying the output
    
    return processes
print(sys.getsizeof(get_processes))