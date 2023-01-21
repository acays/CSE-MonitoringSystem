
import os


#https://www.geeksforgeeks.org/python-get-list-of-running-processes/
def get_processes():
    # Running the aforementioned command and saving its output
    output = os.popen('wmic process get description, processid').read()
    
    # Displaying the output
    print(output)
get_processes()