"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of function create_mysql_db() in Python:
Creates a new MySQL database

param host: host name
param user: user name
param password: password
param db_name: database name to be created
"""
# =================================================================
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode


def create_mysql_db(host, user, password, db_name):
    """
    Creates MySQL Database.

    :param host: host name
    :param user: user name
    :param password: password
    :param db_name: database name to be created
    """
    # Create a connection object
    connection = mysql.connector.connect(host=host,
                                 user=user,
                                 password=password,
                                 autocommit=True)

    print('Connected to DB: {}'.format(host))

    try:

        # Create a cursor object
        cursor = connection.cursor()

        # sql statement to create a pydb
        sql_statement = "CREATE DATABASE IF NOT EXISTS " + db_name

        # execute the create pydb SQL statement through the cursor instance
        cursor.execute(sql_statement)

        print('Successfully created database {}'.format(db_name))

        # SQL query string
        sql_query = "SHOW DATABASES"

        # Execute the sql query
        cursor.execute(sql_query)

        # Fetch all the rows
        database_list = cursor.fetchall()

        for i in database_list:
            if i[0] == db_name:
                print(i[0])

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with user name or password")
        else:
            print(err)

    finally:
        connection.close()

