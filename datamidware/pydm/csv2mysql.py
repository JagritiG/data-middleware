"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of function csv2mysql() in Python:
Imports csv file into mysql pydb

param host: host name
param user: user name
param password: password
param filename: filename to send to pydb
param db_name: name of the pydb -- if pydb already exists, import data
               in the existing pydb, if not exists, create new pydb and import
               data.
param tb_name: name of the table -- if table already exists, add data
               in the existing table, if not exists, create new table and import
               data.

"""
# =================================================================
from __future__ import print_function
import pandas as pd
from .create_mysql_db import create_mysql_db
import mysql.connector
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


def csv2mysql(host, user, password, filename, db_name, tb_name):
    """
    Imports csv file into mysql db

    :param host: host name
    :param user: user name
    :param password: password
    :param filename: filename to send to db
    :param db_name: name of the pydb -- if db already exists, import data
               in the existing pydb, if not exists, create new db and import
               data.
    :param tb_name: name of the table -- if table already exists, add data
               in the existing table, if not exists, create new table and import
               data.
    """

    # Read csv file in pandas DataFrame
    df = pd.read_csv(filename, delimiter=',', encoding='unicode_escape', error_bad_lines=False)
    print(df.shape)

    # Removing/replacing special character from column name with "_"
    # df.columns = df.columns.str.replace('/', ' ')
    df.columns = df.columns.str.replace(r"[^a-zA-Z\d\_]+", "_")
    # df.columns = df.columns.str.replace(' ', '_')

    # if "db_name" already exits
    if exists_db(host, user, password, db_name=db_name):

        # if table already exists
        if exists_tb(host, user, password, db_name=db_name, tb_name=tb_name):
            # insert data to existing table
            insert_etb(host, user, password, df, db_name=db_name, tb_name=tb_name)

        # if table does not exist
        else:

            # create new table and insert data
            insert_ntb(host, user, password, df, db_name=db_name, tb_name=tb_name)

    # if pydb does not exit already
    else:

        # create new pydb
        create_mysql_db(host, user, password, db_name=db_name)

        # create a new table and insert data from dataframe
        insert_ntb(host, user, password, df, db_name=db_name, tb_name=tb_name)


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
    connection = mysql.connector.connect(host=host,
                                 user=user,
                                 password=password)

    connection.autocommit = True

    # Create a cursor object
    cursor = connection.cursor()

    # check if db exists
    sql_query = "SHOW DATABASES"
    cursor.execute(sql_query)

    # Fetch all the rows
    database_list = cursor.fetchall()

    for i in database_list:
        if i[0] == db_name:
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
    connection = mysql.connector.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=db_name)

    connection.autocommit = True

    # Create a cursor object
    cursor = connection.cursor()

    # check if table exists
    sql_query = "SHOW TABLES"
    cursor.execute(sql_query)

    # Fetch all the rows
    table_list = cursor.fetchall()

    for i in table_list:
        if i[0] == tb_name:
            return True

    return False

# =======================================================================
# 1. Implementation of function insert_ntb():
# Creates a new table (ntb) if not exists already and inserts
# data from pandas DataFrame to new table (ntb)
#
# 2. Implementation of function insert_etb():
# Inserts data from pandas DataFrame to existing table (etb).
#
# param host: host name
# param user: user name
# param password: password
# param df: pandas DataFrame to be sent to pydb
# param db_name: name of the pydb where table is created
# param tb_name: name of the existing table/name of the table to create
# =======================================================================


# Insert new values to the existing table
def insert_etb(host, user, password, df, db_name, tb_name):
    """
    Inserts data from pandas DataFrame to existing table (etb).

    :param host: host name
    :param user: user name
    :param password: password
    :param df: pandas DataFrame to be sent to pydb
    :param db_name: name of the pydb
    :param tb_name: name of the existing table
    """

    # Create a connection object
    # dialect+driver://username:password@host:port/pydb
    connect_string = "mysql+pymysql://{}:{}@{}/{}".format(user, password, host, db_name)
    engine = db.create_engine(connect_string, encoding='latin1', echo=True, pool_pre_ping=True)
    # connection = engine.connect()
    session = sessionmaker(bind=engine)()
    metadata = db.MetaData()

    try:

        # create table
        df.to_sql(tb_name, con=engine, index=False, if_exists='append')

        # print the table column names
        tb = db.Table(tb_name, metadata, autoload=True, autoload_with=engine)
        print(tb.columns.keys())

    except Exception as e:
        print('Error: {}'.format(str(e)))

    finally:
        engine.dispose()
        session.close()
        # sys.exit()


# Insert into new table
def insert_ntb(host, user, password, df, db_name, tb_name):
    """
    creates a new table if not exists already and inserts data
    from pandas DataFrame to new table (ntb).

    :param host: host name
    :param user: user name
    :param password: password
    :param df: pandas DataFrame to be sent to pydb
    :param db_name: name of the pydb
    :param tb_name: name of the table to create
    """

    # Create a connection object
    # dialect+driver://username:password@host:port/pydb
    connect_string = "mysql+pymysql://{}:{}@{}/{}".format(user, password, host, db_name)
    engine = db.create_engine(connect_string, encoding='latin1', echo=True, pool_pre_ping=True)
    # connection = engine.connect()
    session = sessionmaker(bind=engine)()
    metadata = db.MetaData()

    try:
        # create table
        df.to_sql(tb_name, con=engine, index=False, if_exists='replace')

        # print the table column names
        tb = db.Table(tb_name, metadata, autoload=True, autoload_with=engine)
        print(tb.columns.keys())

    except Exception as e:
        print('Error: {}'.format(str(e)))

    finally:
        engine.dispose()
        session.close()
        # sys.exit()
