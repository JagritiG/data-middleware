import pandas as pd
import sys
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
    df = pd.read_csv(filename, delimiter=',')
    print(df.head(3))
    print(df.columns)
    # df.columns = df.columns.str.replace('/', ' ')
    df.columns = df.columns.str.replace(r"[^a-zA-Z\d\_]+", "_")
    # df.columns = df.columns.str.replace(' ', '_')
    print(df.columns)

    # Create a connection object
    # dialect+driver://username:password@host:port/pydb
    connect_string = "mysql+pymysql://{}:{}@{}/{}".format(user, password, host, db_name)
    engine = db.create_engine(connect_string, encoding='latin1', echo=True, pool_pre_ping=True)
    # connection = engine.connect()
    metadata = db.MetaData()

    try:
        # create table
        df.to_sql(tb_name, con=engine, index=False, if_exists='replace')

        # print the table column names
        tb = db.Table(tb_name, metadata, autoload=True, autoload_with=engine)
        print(tb.columns.keys())

        # print full table metadata
        # print(repr(metadata.tables[tb_name]))

        # # Equivalent to 'SELECT * FROM complaint'
        # sql_query = db.select([tb_name])
        # execute_result = engine.connect.execute(sql_query)
        # result_set = execute_result.fetchone()
        #
        # print(result_set[:3])

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)


if __name__ == "__main__":

    filename = "/Users/santanusarma/Dropbox/Jagriti/Programming/Data Analysis/data_integration_middleware/dataware/tests/test_data/titanic_short.csv"
    db_name = "titanic"
    host = 'localhost'
    user = 'root'
    password = 'skysh@2018'
    tb_name = "titanic"
    insert_sql_tb(host, user, password, db_name, tb_name, filename)
