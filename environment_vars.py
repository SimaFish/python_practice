# https://www.askpython.com/python/environment-variables-in-python
# https://stackoverflow.com/questions/4906977/how-to-access-environment-variable-values
# https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python
# from os import environ
import os
import sys

# Printing environment variables and their values 1
def list_env_vars_1():
    for var in os.environ:
        print('Var: {0}, Value: {1}'.format(var, os.getenv(var)))

# Printing environment variables and their values 2
def list_env_vars_2():
    for var, value in os.environ.items():
        print(f'{var} = {value}')

# Get environment variable value
def get_env_var_value(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        print('Environment variable "{0}" doesn\'t exist'.format(var_name))
        sys.exit(1)