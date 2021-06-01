import os

# (min_privs) localhost
vars_localhost = {'EXTPACK_HOST': 'localhost',
                  'EXTPACK_PORT': '5432',
                  'EXTPACK_DATABASE': 'ExtPackTestDB',
                  'EXTPACK_USERNAME': 'min_privs',
                  'EXTPACK_PASSWORD': 'min_privs'}

# (min_privs) pg-dba.cjj06khxetlc.us-west-2.rds.amazonaws.com
vars_rds_1 = {'EXTPACK_HOST': 'pg-dba.cjj06khxetlc.us-west-2.rds.amazonaws.com',
              'EXTPACK_PORT': '5432',
              'EXTPACK_DATABASE': 'test_extpack_oseledko',
              'EXTPACK_USERNAME': 'min_privs',
              'EXTPACK_PASSWORD': 'min_privs'}

for env_var in vars_localhost:
    os.system('SETX {0} {1}'.format(env_var, vars_localhost.get(env_var))) # Set as user variable
    os.system("SETX {0} {1} /M".format(env_var, vars_localhost.get(env_var))) # Set as system variable