# `shutil` module provides many functions of high-level operations
# on files and collections of files.
# https://www.geeksforgeeks.org/python-shutil-copyfile-method/
from shutil import copyfile
from subprocess import Popen
import os, time, stat

bteq_glue_tester_path = r'C:\Users\oseledko.a\Desktop\AWS Database Tester\BTEQToAWSGlue'
tester_batch_fpath = r'Settings\generate-batch.xml'
bteq_batch_fpath = r'Scripts\bteq_import_signature_18_skip_repeat_star_pack_x\generate-batch.xml'
test_gen_bat_file = 'generate-test-json.bat'
clear_test_pyfile = 'clear_test.py'

# Source file path
src_file = bteq_glue_tester_path + '\\' + bteq_batch_fpath

# Destination file path
dst_file = bteq_glue_tester_path + '\\' + tester_batch_fpath

# Checking source file exists and is not a directory
try:
    if not os.path.isfile(src_file):
        print('Path is not a file:', src_file)
        time.sleep(1.5)
        quit()
except FileNotFoundError:
    print('File not found:', src_file)
    time.sleep(1.5)
    quit()

# Checking destination file permissions
if os.path.exists(dst_file) and \
   not os.access(dst_file, os.W_OK):
    os.chmod(dst_file, stat.S_IWRITE)

# Copy the content of `src_file` to `dst_file`
copyfile(src_file, dst_file)

# Clear previous test files
Popen(['py', clear_test_pyfile], cwd=bteq_glue_tester_path)

# Launch test generation *.bat file
Popen(bteq_glue_tester_path + '\\' + test_gen_bat_file, cwd=bteq_glue_tester_path)