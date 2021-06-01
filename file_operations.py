import os

# Check a file or directory exists
os.path.exists(r'C:\test_file.txt') # --> True\False

# Check whether a given input is a file
os.path.isfile('test_file.txt') # --> True\False

# Check that a given path points to a directory
os.path.isdir(r'C:\Oracle\admin\simafishdb') # --> True\False

# Check the permissions of a file
os.access('my_file.txt', os.R_OK) # read access --> True\False
os.access('my_file.txt', os.W_OK) # write access --> True\False
os.access('my_file.txt', os.X_OK) # execution access --> True\False
os.access('my_file.txt', os.F_OK) # existance of file --> True\False