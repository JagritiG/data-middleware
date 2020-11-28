from configparser import ConfigParser

# Get the config parser object
config_object = ConfigParser()

config_object["MYSQL"] = {
    "host": "localhost",
    "user": "root",
    "password": "datamidware"
}

# Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)


