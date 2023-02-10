
import os


#https://www.geeksforgeeks.org/python-get-list-of-running-processes/
def get_processes():
    processes = os.popen('wmic process get description, processid').read()
        
    return processes

def save_processes_tofile(name):
    process_file = open(name, "w")
    
    process_file.write(get_processes() + "\n")