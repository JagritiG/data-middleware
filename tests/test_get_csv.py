import os.path
import mysql.connector
from mysql.connector import errorcode
import settings.mysqlconfig as cfg
from datamidware.pydp import get_csv
from datamidware.pydm import create_mysql_db


# Test data url
# 500 Cities: Local Data for Better Health, 2019 release from Data.gov
# url = "https://data.cdc.gov/api/views/6vp6-wxuq/rows.csv?accessType=DOWNLOAD"
url = "https://data.cdc.gov/api/views/k8w5-7ju6/rows.csv?accessType=DOWNLOAD"

# File path to save downloaded csv file
filepath = "./data/"

# Database connection credentials to load data into MySQL database
user_mysql = cfg.mysql["user"]
host_mysql = cfg.mysql["host"]
password_mysql = cfg.mysql["password"]

# Database and table name where data is to be loaded
db_name = "Health"
tb_name = "Nutrition"


def test_get_csv():

    # Create database "Health"
    create_mysql_db.create_mysql_db(host_mysql, user_mysql, password_mysql, db_name)

    # Call get_csv.get_csv()
    get_csv.get_csv(url, filepath, save2db=dict(host=host_mysql, user=user_mysql,
                                                    password=password_mysql, db_type="mysql",
                                                    db_name=db_name, tb_name=tb_name))

    # Check if csv file is saved or not
    assert os.path.isfile("./data/Nutrition__Physical_Activity__and_Obesity_-_Policy_and_Environmental_Data.csv") == True

    # Check if data is loaded into table "Nutrition" or not
    # Create a connection object
    connection = mysql.connector.connect(host=host_mysql,
                                         user=user_mysql,
                                         password=password_mysql,
                                         database=db_name,
                                         autocommit=True)

    try:

        # Create a cursor object
        cursor = connection.cursor()

        # SQL query string
        sql_query1 = "SHOW TABLES"

        # Execute the sql query
        cursor.execute(sql_query1)

        # Fetch all the rows
        table_list = cursor.fetchall()

        for i in table_list:
            if i[0] == tb_name:
                expected_tb = i[0]
                assert expected_tb == "Nutrition"

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with user name or password")
        else:
            print(err)

    finally:
        connection.close()


test_get_csv()








