"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
========================================================================
1. Implementation of function insert_ntb():
Creates a new table (ntb) if not exists already and inserts
data from pandas DataFrame to new table (ntb)

2. Implementation of function insert_etb():
Inserts data from pandas DataFrame to existing table (etb).

param host: host name
param user: user name
param password: password
param df: pandas DataFrame to be sent to pydb
param db_name: name of the pydb where table is created
param tb_name: name of the existing table/name of the table to create

"""
# =======================================================================
from __future__ import print_function
import sys
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


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
