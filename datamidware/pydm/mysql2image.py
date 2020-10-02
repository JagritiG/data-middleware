# Retrieve Image and File stored as a BLOB from MySQL Table
# Write this BLOB binary data on a disk.
# To write this binary data on hard disk we can pass
# the file format in which we want it to be displayed.

import pymysql
import os


# function that can convert image and file into binary data
def write_binary(data, filename):

    # Convert binary data to proper format and write it on Hard Disk
    print(filename)
    with open(filename, 'wb') as file:
        file.write(data)


# Retrieve Image and File stored as a BLOB from MySQL Table
def mysql2image(host, user, password, db_name=None, tb_name=None,
                sql_query=None, file_path=None,
                image_col=None, ext="png"):
    """

    :param host:
    :param user:
    :param password:
    :param db_name:
    :param tb_name:
    :param sql_query:
    :param file_path:
    :param image_col:
    :param ext:
    :return:
    """

    print("Reading BLOB data from mysql table")
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     autocommit=True,
                                     database=db_name)

        cursor = connection.cursor()

        cursor.execute("SHOW COLUMNS FROM {}".format(tb_name))
        record1 = cursor.fetchall()

        # Find column number of the given column name (e.g., image column)
        img_col_num = 0
        for i, row in enumerate(record1):
            # print(i, row[0])
            if row[0] == image_col:
                img_col_num = i

        cursor.execute(sql_query)
        record = cursor.fetchall()

        for row in record:
            # print("Id = ", row[0],)
            # image_name = row[1]
            # print(image_name)
            img = row[img_col_num]
            # print("Size = ", row[3])
            # print("Mod_Date = ", row[4])

            print("Storing image on disk \n")
            if os.path.exists('{}/image_{}.{}'.format(file_path, row[0], ext)):
                old_file_name = '{}/image_{}.{}'.format(file_path, row[0], ext)
                new_file_name = '{}/old_image_{}.{}'.format(file_path, row[0], ext)
                os.rename(old_file_name, new_file_name)
                print("File renamed!")

            file_name = file_path + "image_{}".format(row[0]) + ".{}".format(ext)
            write_binary(img, file_name)
            print('File, {}, has been written successfully'.format(file_name))

        connection.close()
        print("MySQL connection is closed")

    except Exception as e:
        print("Failed to read BLOB data from MySQL table {}".format(e))
