"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of function write_csv() in Python:
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
import sys
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import os


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


