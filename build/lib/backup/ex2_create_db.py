import pymysql
import pandas as pd
import sys
from sqlalchemy import create_engine, types


def create_db(host, user, password, db_name):
    """
    This function load a csv file to MySQL table.
    :param host: host name
    :param user: user name
    :param password: password
    :param: db_name
    """
    # Create a connection object
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 autocommit=True,
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.DictCursor)

    print('Connected to DB: {}'.format(host))

    try:

        # Create a cursor object
        cursor = connection.cursor()

        # sql statement to create a pydb
        sql_statement = "CREATE DATABASE " + db_name

        # execute the create pydb SQL statement through the cursor instance
        cursor.execute(sql_statement)

        print('Successfully created pydb {}'.format(db_name))

        # SQL query string
        sql_query = "SHOW DATABASES"

        # Execute the sql query
        cursor.execute(sql_query)

        # Fetch all the rows
        database_list = cursor.fetchall()

        for db in database_list:
            print(db)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

    finally:
        connection.close()


if __name__ == "__main__":

    filename = "/Users/santanusarma/Dropbox/Jagriti/Programming/Data Analysis/data_integration_middleware/dataware/data/Consumer_Complaints.csv"
    db_name = "consumer"
    host = 'localhost'
    user = 'root'
    password = 'skysh@2018'
    create_db(host, user, password, db_name)
