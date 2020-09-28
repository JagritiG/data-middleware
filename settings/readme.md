The configuration file for Database connection (user, host, port, password):
The file consists of sections, each of which contains keys with values.

A basic configuration file looks like this:

# sample_config.ini

[XXCONFIG]
host = hostname1
user = username1
password = password1

[YYCONFIG]
host = hostname2
user = username2
password = password2

-----------------------------------------------------------------------------------------
The write_config.py have created and saved a configuration file (e.g., sample_config.ini)
The read_config.py shows how to read a config file.
The update_config.py shows how to update key in a config file.

-------------------------------------------------------------------------------
 # Install all dependencies using following command

    pip install -r requirements.txt
