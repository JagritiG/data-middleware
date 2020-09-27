"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of Class mysql_query() in Python:

"""
# =================================================================
from __future__ import print_function
import pymysql
from loguru import logger
import sys


class MySQLDatabase:
    """Database connection class."""

    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.conn = None

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.db_name,
                    autocommit=True,
                    charset="utf8mb4",
                    cursorclass=pymysql.cursors.DictCursor)

        except pymysql.MySQLError as e:
            logger.error(e)
            sys.exit()

        finally:
            logger.info("Connection opened successfully.")

    def select(self, tb_name, row_count="all"):
        """Execute SQL query: SELECT * FROM table.
        Selecting all(or one if row_count="one") rows from the table.

        :param query: SQL query to select rows: SELECT * FROM <table>
        :param row_count: "all" or "one" row. default "all".
        :return list of rows selected.
        """
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                records = []
                query = "SELECT * FROM {}".format(tb_name)
                cur.execute(query)

                if row_count == "one":
                    result = cur.fetchone()

                else:
                    result = cur.fetchall()
                for row in result:
                    records.append(row)
                cur.close()
                return records

        except pymysql.MySQLError as e:
            print('Error: {}'.format(str(e)))

        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logger.info('Database connection closed.')

    def drop_column(self, tb_name, col_name):
        """Drop a column in a table.

        Execute SQL query:

            "ALTER TABLE <table name>
                DROP COLUMN <column name>"

        :param tb_name: The name of the table to modify
        :param col_name: The name of the column to delete from the table.
        :return: number of rows affected after modification
        """
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                query = """ALTER TABLE {}\
                            DROP COLUMN {};""".format(tb_name, col_name)
                cur.execute(query)
                affected = f"{cur.rowcount}' rows affected."
                cur.close()
                return affected

        except pymysql.MySQLError as e:
            print('Error: {}'.format(str(e)))

        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logger.info('Database connection closed.')

    def rename_column(self, tb_name, old_name, new_name, col_def, col_pos=None):
        """Rename a column in a table.

        Execute SQL query:

            "ALTER TABLE <table name>
                CHANGE COLUMN <old name> <new name>
                column_definition
                [ FIRST | AFTER column_name ]"

        :param tb_name: The name of the table to modify
        :param old_name: The column name to rename
        :param new_name: The new name for the column
        :param col_def: The data type and definition of the column (NULL or NOT NULL, etc).
                        You must specify the column definition when renaming the column,
                        even if it does not change.
        :param col_pos: Optional. It tells MySQL where in the table to position the column,
                        if you wish to change its position.
        :return: number of rows affected after modification
        """
        try:
            self.open_connection()
            with self.conn.cursor() as cur:

                if col_pos is not None:

                    query = """ALTER TABLE {}\
                                CHANGE COLUMN {} {}\
                                    {}
                                    {}""".format(tb_name, old_name, new_name, col_def, col_pos)
                else:
                    query = """ALTER TABLE {}\
                                CHANGE COLUMN {} {}\
                                    {}""".format(tb_name, old_name, new_name, col_def)

                cur.execute(query)
                affected = f"{cur.rowcount}' rows affected."
                cur.close()
                return affected

        except pymysql.MySQLError as e:
            print('Error: {}'.format(str(e)))

        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logger.info('Database connection closed.')

    def run_query(self, query):
        """Execute SQL query.

        :param query: SQL query to modify table
        :return: number of rows affected after modification
        """
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                cur.execute(query)
                affected = f"{cur.rowcount}' rows affected."
                cur.close()
                return affected

        except pymysql.MySQLError as e:
            print('Error: {}'.format(str(e)))

        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logger.info('Database connection closed.')


if __name__ == "__main__":

    user = "user"
    host = "host"
    password = "password"
    db_name = "titanic"
    tb_name = "titanic"

    db = MySQLDatabase(host, user, password, db_name)

    # test deb.select()
    rows = db.select(tb_name, row_count="one")
    print(rows)

    # test db.rename_column()
    db.rename_column(tb_name, "SiblingsSpousesAboard", "SiblingsSpousesAboard", "bigint(20) NOT NULL")
    rows = db.select(tb_name, row_count="one")
    print(rows)

    # test db.drop_column()
    db.drop_column(tb_name, "Parents_Children_Aboard")
    rows = db.select(tb_name, row_count="one")
    print(rows)

