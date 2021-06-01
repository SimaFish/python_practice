import os, stat
import shutil

isWOK = False
bteq_glue_path = r'C:\Users\oseledko.a\Desktop\AWS Database Tester\BTEQToAWSGlue'
sct_log_path = r'C:\Users\oseledko.a\AWS Schema Conversion Tool\Log'

path_list = []
# Tester paths
path_list.append(sct_log_path)
path_list.append(bteq_glue_path + r'\Tests')
path_list.append(bteq_glue_path + r'\TestClasses')
path_list.append(bteq_glue_path + r'\Results')
# AWS Glue paths
path_list.append(bteq_glue_path + r'\AWSGlueTests\Values')
# BTEQ paths
path_list.append(bteq_glue_path + r'\BTEQTests\Backup')
path_list.append(bteq_glue_path + r'\BTEQTests\Values')
path_list.append(bteq_glue_path + r'\BTEQTests\Shell')
path_list.append(bteq_glue_path + r'\BTEQTests\Logs')

def remove_readonly(func, path, info):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def remove_file(file):
    try:
        os.remove(file)
    except PermissionError:
        if not isWOK:
            isWOK = True
            os.chmod(file, stat.S_IWRITE)
            remove_file(file)

def delete_dir_content(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir), onerror=remove_readonly)
        for file in files:
            remove_file(os.path.join(root, file))

for path in path_list:
    delete_dir_content(path)