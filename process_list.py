
import os
import sys

#https://www.geeksforgeeks.org/python-get-list-of-running-processes/
def get_processes():
    processes = os.popen('wmic process get description, processid').read()
        
    return processes
# print(sys.getsizeof(get_processes))