import os, time
import sys
import boto3
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, SubElement, Element, tostring

base_dir_path = r'C:\Users\oseledko.a\Desktop\AWS Database Tester\BTEQToAWSGlue'
xml_batch_path = base_dir_path + r'\Settings\apply-batch.xml'
tests_path = base_dir_path + r'\Tests'

# Parse XML batch file and extract connection keys
try:
    xml_batch_tree = ET.parse(xml_batch_path)
except FileNotFoundError:
    print('File not found:', xml_batch_path)
    time.sleep(1.5)
    quit()

for node in xml_batch_tree.findall('.//ConnectCommand'):
    if node.attrib['vendor'].upper() == "REDSHIFT":
        aws_access_key = node.attrib['accessKey']
        aws_secret_key = node.attrib['secretKey']

# Connect to AWS Glue
client = boto3.client(
    service_name='glue',
    region_name='us-west-2',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# Get test class ID from XML batch file
for node in xml_batch_tree.findall('.//CreateTestClassCommand'):
    test_class_file = node.attrib['jsonFilePath']
    test_class_id = os.path.splitext(os.path.basename(test_class_file))[0]

try:
    test_class_json = open(test_class_file, "r")
    json_data = json.load(test_class_json)
except FileNotFoundError:
    print('File not found:', test_class_file)
    time.sleep(1.5)
    quit()

# Collect job names from tests
jobs = set()
for element_data in json_data['tests']:
    if element_data['test-id']:
        with open(tests_path + '\\' + element_data['test-id'] + '.json', "r") as test_file:
            data_test_json = json.load(test_file)
            job_name = data_test_json['test-sql']['target'].strip()
            jobs.add(job_name)

# Delete jobs in AWS Glue
for job_name in tuple(jobs):
    response = client.delete_job(JobName=job_name)

print(response)
time.sleep(1.5)