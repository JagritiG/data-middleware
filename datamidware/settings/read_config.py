# Read config file
from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read('sample_config.ini')

# Get the password
mysql_cred = config_object["XXCONFIG"]
print("Password is {}".format(mysql_cred["password"]))


