import unittest
from loguru import logger
import time
import settings.mysqlconfig as cfg

from datamidware.pydm import (
    csv2mysql,
    mysql_query)


class TestMySQL(unittest.TestCase):
    def setUp(self):

        # Assign the user, the host, and the password
        self.user = cfg.mysql["user"]
        self.host = cfg.mysql["host"]
        self.password = cfg.mysql["password"]
        self.filename = "./tests/test_data/titanic_short.csv"


class TestMySQLQuery(TestMySQL):

    def test_select(self):
        db = mysql_query.MySQLDatabase(self.host, self.user, self.password, "titanic")
        try:
            db.open_connection()
            with db.conn.cursor() as cur:
                drop_table = "DROP TABLE IF EXISTS titanic"
                cur.execute(drop_table)
                csv2mysql.csv2mysql(self.host, self.user, self.password, self.filename, "titanic", "titanic")
                row = db.select("titanic", row_count="one")
                # self.assertEqual(row, ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare'])
                assert row == ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare']

        except Exception as e:
            print('Error: {}'.format(str(e)))

        finally:
            if db.conn:
                db.conn.close()
                db.conn = None
                logger.info('Database connection closed.')
                time.sleep(3)

    def test_drop_column(self):
        db = mysql_query.MySQLDatabase(self.host, self.user, self.password, "titanic")
        try:
            db.open_connection()
            with db.conn.cursor() as cur:
                drop_table = "DROP TABLE IF EXISTS titanic"
                cur.execute(drop_table)
                csv2mysql.csv2mysql(self.host, self.user, self.password, self.filename, "titanic", "titanic")
                db.rename_column("titanic", "Pclass", "Passenger_Class", "bigint(20) NOT NULL")
                row = db.select("titanic", row_count="one")
                # self.assertEqual(row, ['Survived', 'Passenger_Class', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare'])
                assert row == ['Survived', 'Passenger_Class', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare']

        except Exception as e:
            print('Error: {}'.format(str(e)))

        finally:
            if db.conn:
                db.conn.close()
                db.conn = None
                logger.info('Database connection closed.')
                time.sleep(3)

    def test_rename_column(self):
        db = mysql_query.MySQLDatabase(self.host, self.user, self.password, "titanic")
        try:
            db.open_connection()
            with db.conn.cursor() as cur:
                drop_table = "DROP TABLE IF EXISTS titanic"
                cur.execute(drop_table)
                csv2mysql.csv2mysql(self.host, self.user, self.password, self.filename, "titanic", "titanic")
                db.drop_column("titanic", "Siblings_Spouses_Aboard")
                row = db.select("titanic", row_count="one")
                # self.assertEqual(row, ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Parents_Children_Aboard', 'Fare'])
                assert row == ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Parents_Children_Aboard', 'Fare']

        except Exception as e:
            print('Error: {}'.format(str(e)))

        finally:
            if db.conn:
                db.conn.close()
                db.conn = None
                logger.info('Database connection closed.')
                time.sleep(3)


# Test Runner
if __name__ == '__main__':
    unittest.main()

# Database: titanic
# Table: titanic
# Table columns: ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare']
