"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
====================================================================
Checks if given pydb and table already exists or not

param host: host name
param user: user name
param password: password
param db_name: filename to send to pydb
param tb_name: name of the table where data will be stored

"""
# =================================================================
import pymysql
import pandas as pd
import sys


def exists_db(host, user, password, db_name):
    """
    Return True if pydb exists, else return False.

    :param host: host
    :param user: user
    :param password: password
    :param db_name: pydb name to check if exists or not
    :return: True if exists, else return False
    """
    # Create a connection object
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 autocommit=True,
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.DictCursor)

    # print('Connected to DB: {}'.format(host))

    # Create a cursor object
    cursor = connection.cursor()

    # check if pydb exists
    sql_query = "SHOW DATABASES"
    cursor.execute(sql_query)

    for db in cursor:
        # print(db.values())
        for val in db.values():
            if val == db_name:
                return True

    return False


def exists_tb(host, user, password, db_name, tb_name):
    """
    Return True if table exists, else return False.

    :param host: host
    :param user: user
    :param password: password
    :param db_name: name of the pydb
    :param tb_name: table name to check if exists or not
    :return: True if exists, else return False
    """
    # Create a connection object
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=db_name,
                                 autocommit=True,
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.DictCursor)

    # print('Connected to DB: {}'.format(host))

    # Create a cursor object
    cursor = connection.cursor()

    # check if table exists
    sql_query = "SHOW TABLES"
    cursor.execute(sql_query)

    for tb in cursor:
        # print(tb.values())
        for val in tb.values():
            if val == tb_name:
                return True

    return False
