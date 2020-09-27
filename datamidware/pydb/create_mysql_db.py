"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of function create_mysql_db() in Python:
Creates a new MySQL pydb

param host: host name
param user: user name
param password: password
param db_name: pydb name to be created
"""
# =================================================================
from __future__ import print_function
import pymysql


def create_mysql_db(host, user, password, db_name):
    """
    Creates MySQL Database.

    :param host: host name
    :param user: user name
    :param password: password
    :param db_name: pydb name to be created
    """
    # Create a connection object
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 autocommit=True,
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.DictCursor)

    print('Connected to DB: {}'.format(host))

    try:

        # Create a cursor object
        cursor = connection.cursor()

        # sql statement to create a pydb
        sql_statement = "CREATE DATABASE IF NOT EXISTS " + db_name

        # execute the create pydb SQL statement through the cursor instance
        cursor.execute(sql_statement)

        print('Successfully created pydb {}'.format(db_name))

        # SQL query string
        sql_query = "SHOW DATABASES"

        # Execute the sql query
        cursor.execute(sql_query)

        # Fetch all the rows
        database_list = cursor.fetchall()

        for db in database_list:
            print(db)

    except Exception as e:
        print("Failed to connect.")
        print('Error: {}'.format(str(e)))

    finally:
        connection.close()

