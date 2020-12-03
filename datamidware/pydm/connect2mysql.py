import mysql.connector
import settings.mysqlconfig as cfg
from mysql.connector import errorcode


def connect2mysql():
    try:
        connection = mysql.connector.connect(
            host=cfg.mysql["host"],
            user=cfg.mysql["user"],
            passwd=cfg.mysql["password"]
        )

        print("Successfully connected to MySQL")

        # # Create a cursor object
        # cursor = connection.cursor()
        #
        # #check if exists
        # sql_query = "SHOW DATABASES"
        # cursor.execute(sql_query)
        #
        # # Fetch all the rows
        # database_list = cursor.fetchall()
        # print(database_list)
        #
        # for i in database_list:
        #     print(i[0])

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        connection.close()


