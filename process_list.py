
import os

def get_processes():
    processes = os.popen('wmic process get description, processid').read()
        
    return processes

def save_processes_to_file(file_name):
    process_file = open(file_name, "w")
    
    process_file.write(get_processes() + "\n")