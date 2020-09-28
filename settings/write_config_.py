from configparser import ConfigParser

# Get the config parser object
config_object = ConfigParser()

config_object["XXCONFIG"] = {
    "host": "hostname1",
    "user": "username1",
    "password": "password1"
}

config_object["YYCONFIG"] = {
    "host": "hostname2",
    "user": "username2",
    "password": "password2"
}

# Write the above sections to config.ini file
with open('sample_config.ini', 'w') as conf:
    config_object.write(conf)


