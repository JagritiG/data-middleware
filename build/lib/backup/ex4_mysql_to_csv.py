from __future__ import print_function
import csv
import pandas as pd
import sys
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import datetime


def write_csv(host, user, password, db_name, tb_name, file_path):

    """
    Writes table data into csv file.

    :param host:
    :param user:
    :param password:
    :param filepath:
    :param db_name:
    :param tb_name:
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

        # Retrieve table data: 'SELECT * FROM complaint'
        sql_query = 'SELECT * FROM complaint'
        df = pd.read_sql(sql_query, connection)
        print(df.head())

        # right to csv
        file_name = file_path + "{}_{}".format(tb_name, datetime.datetime.now().strftime('%d-%m-%Y:%H:%M'))
        df.to_csv(file_name, encoding="utf-8", header=True, doublequote=True,
                  sep=',', index=False)
        print('File, {}, has been created successfully'.format(file_name))

    except Exception as e:
        print('Error: {}'.format(str(e)))

    finally:
        engine.dispose()
        session.close()
        # sys.exit(1)


if __name__ == "__main__":

    file_path = "/Users/santanusarma/Dropbox/Jagriti/Programming/Data Analysis/data_integration_middleware/dataware/data/"
    db_name = "consumer"
    host = 'localhost'
    user = 'root'
    password = 'skysh@2018'
    tb_name = "complaint"
    write_csv(host, user, password, db_name, tb_name, file_path)


