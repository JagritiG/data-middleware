import mysql.connector
from mysql.connector import errorcode
import settings.mysqlconfig as cfg
from datamidware.pydm import create_mysql_db


# Database connection credentials to create MySQL database
user_mysql = cfg.mysql["user"]
host_mysql = cfg.mysql["host"]
password_mysql = cfg.mysql["password"]

# Database and table name to be loaded
db_name = "TestDB"


def test_create_mysql_db():

    # Create database TestDB
    create_mysql_db.create_mysql_db(host_mysql, user_mysql, password_mysql, db_name)

    # Check if Database is created or not
    # Create a connection object
    connection = mysql.connector.connect(host=host_mysql,
                                         user=user_mysql,
                                         password=password_mysql,
                                         autocommit=True)

    try:

        # Create a cursor object
        cursor = connection.cursor()

        # SQL query string
        sql_query = "SHOW DATABASES"

        # Execute the sql query
        cursor.execute(sql_query)

        # Fetch all the rows
        database_list = cursor.fetchall()

        for i in database_list:
            if i[0] == db_name:
                expected_db = i[0]
                assert expected_db == "TestDB"

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with user name or password")
        else:
            print(err)

    finally:
        connection.close()
