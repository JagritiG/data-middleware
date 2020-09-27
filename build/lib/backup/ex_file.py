import pymysql
import pandas as pd
import sys
from sqlalchemy import create_engine, types


def csv_to_mysql(load_sql, host, user, password):
    """
    This function load a csv file to MySQL table according to
    the load_sql statement.
    :param load_sql: sql command
    :param host: host name
    :param user: user name
    :param password: password
    :return:
    """

    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                autocommit=True,
                                local_infile=1)
        print('Connected to DB: {}'.format(host))

        # Create cursor and execute Load SQL
        cursor = con.cursor()
        cursor.execute(load_sql)
        print('Successfully loaded the table from csv.')
        con.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

# Execution Example

load_sql = "LOAD DATA LOCAL INFILE '/tmp/city.csv' INTO TABLE usermanaged.city\
 FIELDS TERMINATED BY ',' ENCLOSED BY '' IGNORE 1 LINES;"
host = 'host url'
user = 'username'
password = 'password'
csv_to_mysql(load_sql, host, user, password)
