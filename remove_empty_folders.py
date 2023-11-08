'''
This script will delete all empty folders and sub folders in the folder that the script is being executed in.
Inspired from : https://stackoverflow.com/questions/22001216/scan-files-recursively-and-delete-empty-directories-in-python

HOW TO USE :
- Place the script in the folder you want to clean.
- Execute the script.
- The deleted folders are saved to a text file that is created by the script.
'''

import os

# declare the root directory
root_dir = os.getcwd() + '/'

# initialize the counters
empty_count = 0
used_count = 0

# Set the file to write to. 'x' will indicate to create a new file and open it for writing
outfile = open(f'{root_dir}deleted_directories_log.txt', 'x')
for curdir, subdirs, files in os.walk(root_dir):
    if len(subdirs) == 0 and len(files) == 0: # check for empty directories. len(files) == 0 may be overkill
        empty_count += 1 # increment empty_count
        print('Empty directory: {}'.format(curdir), file = outfile) # add empty results to file
        os.rmdir(curdir) # delete the directory
    elif len(subdirs) > 0 and len(files) > 0: #check for used directories
        used_count += 1 # increment used_count
        print('Used directory: {}'.format(curdir), file = outfile) # add used results to file

# add the counters to the file
print('empty_count: {}\nused_count: {}'.format(empty_count, used_count), file = outfile) 
outfile.close() #close the file
