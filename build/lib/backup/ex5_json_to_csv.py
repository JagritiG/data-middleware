import json
import pandas as pd
from pandas.io.json import json_normalize
import sys
from pprint import pprint
from sqlalchemy.types import Integer

import sqlalchemy as db


def insert_sql_tb(host, user, password, db_name, tb_name, filename):
    """
    This function load a csv file to MySQL table according to
    the load_sql statement.
    :param host: host name
    :param user: user name
    :param password: password
    :param: db_name
    """
    # import data as pandas dataframe
    with open(filename, 'r') as f:
        data = json.load(f)

    pprint(data)
    print(data.keys())
    pprint(data["dates"].keys())
    results = data["results"]
    df = pd.json_normalize(results)
    print(df.head())
    # df = pd.json_normalize(data[tb_name])
    # df = pd.json_normalize(data, record_path="{}".format(tb_name), max_level = 2)
    # print(df.columns)
    # for i in range(len(df.columns)):
    #     if type(df.iloc[0][i]) == list:
    #         col_name = df.columns[i]
    #         df["{}".format(col_name)] = [','.join(map(str, l)) for l in df["{}".format(col_name)]]
        # print(type(df.iloc[0][i]))

    # Create a connection object
    # dialect+driver://username:password@host:port/pydb
    # connect_string = "mysql+pymysql://{}:{}@{}/{}".format(user, password, host, db_name)
    # engine = db.create_engine(connect_string, encoding='latin1', echo=True, pool_pre_ping=True)
    # # connection = engine.connect()
    # metadata = db.MetaData()
    #
    # try:
    #     # create table
    #     df.to_sql(tb_name, con=engine, index=False, if_exists='replace')
    #
    #     # print the table column names
    #     tb = db.Table(tb_name, metadata, autoload=True, autoload_with=engine)
    #     print(tb.columns.keys())
    #
    # except Exception as e:
    #     print('Error: {}'.format(str(e)))
    #     # sys.exit(1)


if __name__ == "__main__":

    filename = "/Users/santanusarma/Dropbox/Jagriti/Programming/Data Analysis/data_integration_middleware/dataware/data/raw_data/tmdb_page1.json"
    db_name = "tmdb"
    host = 'localhost'
    user = 'root'
    password = 'skysh@2018'
    tb_name = "results"
    insert_sql_tb(host, user, password, db_name, tb_name, filename)
