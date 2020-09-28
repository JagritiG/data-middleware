# Update a key in config file
from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("sample_config.ini")


# Get the MYSQLCONFIG section
mysql_cred = config_object["XXCONFIG"]

# Update the password
mysql_cred["password"] = "newpassword"

# Write changes back to file
with open('sample_config.ini', 'w') as conf:
    config_object.write(conf)


