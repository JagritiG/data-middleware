"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of function json2mysql() in Python:
Import json file and converts json file into pandas DataFrame.
Sends DataFrame to mysql pydb table

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
param key: json key name to create mysql table
"""
# =================================================================
from __future__ import print_function
import json
import pandas as pd
from pandas.io.json import json_normalize
from .create_mysql_db import create_mysql_db
import pymysql
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


def json2mysql(host, user, password, filename, db_name, tb_name, key=None):
    """
    Import json file and converts json file into pandas DataFrame.
    Sends DataFrame to mysql database table

    param host: host name
    param user: user name
    param password: password
    param filename: filename to send to db
    param db_name: name of the db -- if db already exists, import data
                   in the existing pydb, if not exists, create new db and import
                   data.
    param tb_name: name of the table -- if table already exists, add data
                   in the existing table, if not exists, create new table and import
                   data.
    param key: json key name to create mysql table
    """

    # import data as pandas dataframe
    with open(filename, 'r') as f:
        data = json.load(f)

    # if specific json key is given to convert into dataframe
    if key is not None:
        df = pd.json_normalize(data[key], sep='_')

    else:  # if key is not given
        df = pd.json_normalize(data, sep='_')

    # Removing/replacing special character from column name with "_"
    # df.columns = df.columns.str.replace('/', ' ')
    df.columns = df.columns.str.replace(r"[^a-zA-Z\d\_]+", "_")
    # df.columns = df.columns.str.replace(' ', '_')

    # check if any column's datatype is a list or not
    # if column holds list, convert it to string- to handle -
    # Error: (pymysql.err.OperationalError) (1241, 'Operand should contain 1 column(s)')
    for i in range(len(df.columns)):
        if type(df.iloc[0][i]) == list:
            col_name = df.columns[i]
            df["{}".format(col_name)] = [','.join(map(str, l)) for l in df["{}".format(col_name)]]

    # if pydb "db_name" already exits
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
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 autocommit=True,
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.DictCursor)

    # print('Connected to DB: {}'.format(host))

    # Create a cursor object
    cursor = connection.cursor()

    # check if db exists
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
