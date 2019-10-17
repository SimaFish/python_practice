# For operations on files within OS environment.
import os

# The print() function prints the specified message to the screen, or other standard output device.
# The message can be a string, or any other object.
# The object will be converted into a string before written to the screen.
# https://www.w3schools.com/python/ref_func_print.asp

# Print single object
print('hello')

# Print several objects
# Notice, the values are separated by ' ' (space)
print('hello', 'world', True, 3.8)

# Print several objects separated by ','
# Default separator value: ' ' (space)
print('hello', 'world', True, 3.8, sep=',')

# Print several objects separated by '_'
# End printed string with ';'. Default ending is '\n' (new line)
print('hello', 'world', True, 3.8, sep='_', end=';')

# Print objects to the file by specifying the file parameter
src_file = open('E:\\log_python.txt', 'w')
print('Pretty cool, huh!', end=' end;', file=src_file)
src_file.close()
# os.remove('E:\\log_python.txt')

# https://eulertech.wordpress.com/2017/10/30/sys-out-flush-in-python/
print('\nImmediate unbuffered message', flush=True)