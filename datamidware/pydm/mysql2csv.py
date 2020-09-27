"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of function mysql2csv() in Python:
it exports csv file from mysql pydb

param host: host name
param user: user name
param password: password
param file_path: file path to save csv file
param db_name: name of the pydb from where data will be exported
param tb_name: name of the table from where data will be exported

"""
# =================================================================
from __future__ import print_function
import pandas as pd
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import os
import pymysql


def mysql2csv(host, user, password, file_path, db_name, tb_name):
    """
    If given db exists, check for given table, if table exists,
    call function export_as_csv() which writes csv file from table data.
    If given db or table does not exists, raise importError.

    :param host: host name
    :param user: user name
    :param password: password
    :param file_path: file path to save csv file
    :param db_name: name of the pydb from where data will be exported
    :param tb_name: name of the table from where data will be exported
    """

    # if db "db_name" exits
    try:
        if exists_db(host, user, password, db_name=db_name):

            # if table already exists
            if exists_tb(host, user, password, db_name=db_name, tb_name=tb_name):
                # export data
                export_as_csv(host, user, password, file_path, db_name, tb_name)

            # if table does not exist, raise error
            else:

                raise ImportError("table {} does not exist.".format(tb_name))

        # if pydb does not exist, raise error
        else:
            raise ImportError("pydb {} does not exist.".format(db_name))

    except Exception as e:
        print('Error: {}'.format(str(e)))


def export_as_csv(host, user, password, file_path, db_name, tb_name):
    """
    Writes table data into csv file.

    :param host: host name
    :param user: user name
    :param password: password
    :param file_path: file path to save csv file
    :param db_name: name of the pydb from where data will be exported
    :param tb_name: name of the table from where data will be exported
    """

    # Create a connection object
    # dialect+driver://username:password@host:port/pydb
    connect_string = "mysql+pymysql://{}:{}@{}/{}".format(user, password, host, db_name)
    engine = db.create_engine(connect_string, encoding='latin1', echo=True, pool_pre_ping=True)
    connection = engine.connect()
    session = sessionmaker(bind=engine)()
    metadata = db.MetaData()

    try:
        # print the table column names
        tb = db.Table(tb_name, metadata, autoload=True, autoload_with=engine)
        print(tb.columns.keys())

        # Retrieve table data: 'SELECT * FROM table'
        sql_query = 'SELECT * FROM {}'.format(tb_name)
        df = pd.read_sql(sql_query, connection)
        print(df.head())

        # right to csv
        if os.path.exists('{}/{}.csv'.format(file_path, tb_name)):
            old_file_name = '{}/{}.csv'.format(file_path, tb_name)
            new_file_name = '{}/old_{}.csv'.format(file_path, tb_name)

            os.rename(old_file_name, new_file_name)
            print("File renamed!")

        file_name = file_path + "{}".format(tb_name) + ".csv"
        df.to_csv(file_name, encoding="utf-8", header=True, doublequote=True,
                  sep=',', index=False)
        print('File, {}, has been created successfully'.format(file_name))

    except Exception as e:
        print('Error: {}'.format(str(e)))

    finally:
        engine.dispose()
        session.close()
        # sys.exit()


# ====================================================================
# Checks if given pydb and table already exists or not
#
# param host: host name
# param user: user name
# param password: password
# param db_name: filename to send to pydb
# param tb_name: name of the table where data will be stored
# ====================================================================


# Checks if given pydb already exists or not
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


# Checks if given table already exists or not
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
