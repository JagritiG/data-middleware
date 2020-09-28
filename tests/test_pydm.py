import unittest2
import os.path
from loguru import logger
import time
from configparser import ConfigParser

from datamidware.pydm import (
    file2db,
    csv2mysql,
    json2mysql,
    db2file,
    mysql_query)


# Read config.ini file
config_object = ConfigParser()
config_object.read('./settings/config.ini')
mysql_cred = config_object["MYSQL"]


class TestDataBase(unittest2.TestCase):
    def setUp(self):

        # Get the user, the host, and the password from config.ini file
        self.user_mysql = mysql_cred["user"]
        self.host_mysql = mysql_cred["host"]
        self.password_mysql = mysql_cred["password"]

        self.filename_csv = "./tests/test_data/titanic_short.csv"
        self.filename_json = "./tests/test_data/product.json"
        self.output_file_path = "./tests/test_result/"


class TestDataBaseCreation(TestDataBase):

    def test_file2db(self):
        """Test file2db() function"""

        try:
            file2db.file2db(self.host_mysql, self.user_mysql, self.password_mysql, self.filename_csv, "titanic", "titanic", "csv", "mysql")

        except Exception as e:
            print('Error: {}'.format(str(e)))

        else:
            db = mysql_query.MySQLDatabase(self.host_mysql, self.user_mysql, self.password_mysql, "titanic")
            try:
                db.open_connection()
                with db.conn.cursor() as cur:
                    row = db.select("titanic", row_count="one")
                    self.assertEqual(row, ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare'])
                    drop_database = "DROP DATABASE titanic"
                    cur.execute(drop_database)
            except Exception as e:
                print('Error: {}'.format(str(e)))

            finally:
                if db.conn:
                    db.conn.close()
                    db.conn = None
                    logger.info('Database connection closed.')
                    time.sleep(3)

    def test_csv2mysql(self):
        """Test csv2mysql() function"""
        try:
            csv2mysql.csv2mysql(self.host_mysql, self.user_mysql, self.password_mysql, self.filename_csv, "titanic", "titanic")

        except Exception as e:
            print('Error: {}'.format(str(e)))

        else:
            db = mysql_query.MySQLDatabase(self.host_mysql, self.user_mysql, self.password_mysql, "titanic")
            try:
                db.open_connection()
                with db.conn.cursor() as cur:
                    row = db.select("titanic", row_count="one")
                    self.assertEqual(row, ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare'])
                    drop_database = "DROP DATABASE titanic"
                    cur.execute(drop_database)
            except Exception as e:
                print('Error: {}'.format(str(e)))

            finally:
                if db.conn:
                    db.conn.close()
                    db.conn = None
                    logger.info('Database connection closed.')
                    time.sleep(3)

    def test_json2mysql(self):
        """Test json2mysql() function"""
        try:
            json2mysql.json2mysql(self.host_mysql, self.user_mysql, self.password_mysql, self.filename_json, "product", "product", key=None)

        except Exception as e:
            print('Error: {}'.format(str(e)))

        else:
            db = mysql_query.MySQLDatabase(self.host_mysql, self.user_mysql, self.password_mysql, "product")
            try:
                db.open_connection()
                with db.conn.cursor() as cur:
                    row = db.select("product", row_count="one")
                    self.assertEqual(row, ['Product_0', 'Product_1', 'Product_2', 'Product_3',
                                           'Price_0', 'Price_1', 'Price_2', 'Price_3'])
                    drop_database = "DROP DATABASE product"
                    cur.execute(drop_database)
            except Exception as e:
                print('Error: {}'.format(str(e)))

            finally:
                if db.conn:
                    db.conn.close()
                    db.conn = None
                    logger.info('Database connection closed.')
                    time.sleep(3)

    def test_db2file(self):
        """Test db2file() function."""
        try:
            db2file.db2file(self.host_mysql, self.user_mysql, self.password_mysql, self.output_file_path, "titanic", "titanic", "csv", "mysql")
            self.assertTrue(os.path.isfile(r"{}/titanic.csv".format(self.output_file_path)), True)

        except Exception as e:
            print('Error: {}'.format(str(e)))


# Test Runner
if __name__ == '__main__':
    unittest2.main()


# Database: titanic
# Table: titanic
# Table columns: ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare']


# Database: tmdb
# Table: tmdb_results
# Table columns: ['popularity', 'vote_count', 'poster_path', 'id', 'adult', 'backdrop_path', 'original_language', 'original_title', 'genre_ids', 'title', 'vote_average', 'overview', 'release_date', 'video']
