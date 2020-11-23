# Insert Image and File as a BLOB data into MySQL Table

import pymysql
import os
import time


# Insert Image file as a BLOB data into MySQL Table from disk/directory
def image2mysql(host, user, password, db_name=None, tb_name=None, dir_path=None, ext=None):
    """
    Insert images from disk or directory to mysql table.

    :param host:
    :param user:
    :param password:
    :param db_name:
    :param tb_name:
    :param dir_name:
    :return:
    """

    try:
        if ext:

            id = 1
            for filename in os.listdir(dir_path):
                if filename.endswith(".{}".format(ext)):
                    file = os.path.join(dir_path, filename)
                    head_tail = os.path.split(file)
                    # print(head_tail[0], head_tail[1])
                    img_name = os.path.splitext(head_tail[1])[0]

                    # return file size in bytes
                    file_size = os.path.getsize(file)

                    # os.path.getmtime(file) return modification time in secs
                    # time.localtime([secs]) converts a time expressed in seconds to local time
                    mod_date = time.localtime(os.path.getmtime(file))
                    # print(img_name, file_size, mod_date)
                    to_mysql(host, user, password, db_name, tb_name, id, img_name, file, file_size, mod_date)
                    id += 1

                continue

        else:
            id = 1
            for filename in os.listdir(dir_path):
                if filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".pdf") \
                        or filename.endswith(".svg") or filename.endswith(".eps") or filename.endswith(".webp"):
                    file = os.path.join(dir_path, filename)
                    head_tail = os.path.split(file)
                    # print(head_tail[0], head_tail[1])
                    img_name = os.path.splitext(head_tail[1])[0]

                    # return file size in bytes
                    file_size = os.path.getsize(file)

                    # os.path.getmtime(file) return modification time in secs
                    # time.localtime([secs]) converts a time expressed in seconds to local time
                    mod_date = time.localtime(os.path.getmtime(file))
                    # print(img_name, file_size, mod_date)
                    to_mysql(host, user, password, db_name, tb_name, id, img_name, file, file_size, mod_date)
                    id += 1

                continue

    except Exception as e:
        print("Failed inserting BLOB data into MySQL table {}".format(e))


# Insert image file as BLOB into mysql database
def to_mysql(host, user, password, db_name=None, tb_name=None, id=None,
                img_name=None, filename=None, size=None, mod_date=None):
    """

    :param host:
    :param user:
    :param password:
    :param db_name:
    :param tb_name:
    :param id:
    :param img_name:
    :param filename:
    :param size:
    :param mod_date:
    :return:
    """
    print("Inserting BLOB into table")
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     autocommit=True,
                                     database=db_name,
                                     cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()
        # if table exists, insert data avoiding duplicate
        if exists_tb(host, user, password, db_name, tb_name):

            sql_query = "INSERT INTO {} VALUES (%s, %s, %s, %s, %s)".format(tb_name)
            # convert image to binary data
            file = dig2binary(filename)

            # Convert data into tuple format
            insert_blob_tuple = (id, img_name, file, size, mod_date)
            result = cursor.execute(sql_query, insert_blob_tuple)
            connection.commit()
            print("Image inserted successfully as a BLOB into {} table".format(tb_name), result)
            connection.close()
            print("MySQL connection is closed")

        # if table does not exist
        else:

            # create new table and insert data
            create_tb(host, user, password, db_name, tb_name)
            sql_query = "INSERT INTO {} VALUES (%s, %s, %s, %s, %s)".format(tb_name)
            # convert image to binary data
            file = dig2binary(filename)

            # Convert data into tuple format
            insert_blob_tuple = (id, img_name, file, size, mod_date)
            result = cursor.execute(sql_query, insert_blob_tuple)
            connection.commit()
            print("Image inserted successfully as a BLOB into {} table".format(tb_name), result)
            connection.close()
            print("MySQL connection is closed")

    except Exception as e:
        print("Failed inserting BLOB data into MySQL table {}".format(e))


# function that can convert image and file into binary data
def dig2binary(filename):

    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data


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


# Create table "image" for figures
def create_tb(host, user, password, db_name, tb_name):
    """
    Create image table.

    :param host:
    :param user:
    :param password:
    :param db:
    :param tb:
    :return:
    """
    # Create a connection object
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=db_name,
                                 autocommit=True)

    # print('Connected to DB: {}'.format(host))

    # Create a cursor object
    cursor = connection.cursor()

    # create table "image"
    sql_query = "CREATE TABLE {} (id INT, " \
                "img_name VARCHAR(100), " \
                "image LONGBLOB, " \
                "size DOUBLE, " \
                "mod_date DATETIME, " \
                "UNIQUE KEY (img_name))".format(tb_name)

    cursor.execute(sql_query)

    # Check table is created or not
    sql_query_show_tb = "SHOW TABLES"
    cursor.execute(sql_query_show_tb)

    for tb in cursor:
        print(tb)

    return False
