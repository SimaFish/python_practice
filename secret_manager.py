import boto3
import json
import environment_vars as env_vars

# Name of the secret
SECRET_NAME = 'DBE.SOURCE.ORACLE_19'

# Getting AWS access credentials
AWS_ACCESS_KEY_ID = env_vars.get_env_var_value('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env_vars.get_env_var_value('AWS_SECRET_ACCESS_KEY')
AWS_REGION_NAME = env_vars.get_env_var_value('AWS_REGION_NAME')

# Getting AWS Secrets Manager client
aws_client = boto3.client(
    service_name = 'secretsmanager',
    region_name = AWS_REGION_NAME,
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

# Obtaining Secrets Manager response
secret_value_data = aws_client.get_secret_value(
    SecretId = SECRET_NAME
)

secret_json = json.loads(secret_value_data['SecretString'])

for key in secret_json:
    print(f'{key} = {secret_json[key]}')









