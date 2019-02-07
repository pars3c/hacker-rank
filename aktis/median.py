import os
import numpy as np

results = {}
path = 'running-median/'
input_files = []

custom_directory = 'custom-running-median/'


try:
    os.makedirs(custom_directory) # Try to create directory
except:
    pass # If the directory is already existent pass on to the next line of the script

for i in os.listdir(path): # Check all the files inside the folder (running-median)
    if os.path.isfile(os.path.join(path,i)) and i.startswith('input'):
        # If those files start with input add to the array (input_files)
        input_files.append(i)

input_files = sorted(input_files) # Sort the (input_files) list to start from input00.txt to input04.txt

for input_file in input_files:
    with open(path + input_file) as inputfile:
        # Insert all the values of each input file inside a dictionary with the key name as the filename
        results[input_file] = inputfile.read().split('\n') 
        
    try:
        os.remove(custom_directory  + input_file.replace('input', 'output'))
        # If the script is running a second time and it finds files inside (custom-running-median) directory delete them before adding *
        # Duplicated values 
    except:
        pass # If there are no files inside (custom-running-median) directory go on to the next script
    for i in range(1, int(results[input_file][0]) + 1):
            arr = np.array(results[input_file][1:i+1]).astype(np.float) # Increment the length of results in each iteration

            with open(custom_directory  + input_file.replace('input', 'output'), 'a') as the_file:
                the_file.write(str(np.median(arr)) + '\n')

    