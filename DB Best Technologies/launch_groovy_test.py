import os

ext_pack_dir = r'D:\DB Best Projects\GitLab\sct-extension-pack'
ora_pg_dir = r'PostgreSQL\Oracle\objects'

os.chdir(ext_pack_dir + '\\' + ora_pg_dir)

os.system('.\..\..\..\gradlew.bat test --tests "com.sct.TestStripSqlComments"')