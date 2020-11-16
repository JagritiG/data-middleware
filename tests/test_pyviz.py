import unittest
import os.path
from loguru import logger
import time
from configparser import ConfigParser

from datamidware.pydm import (
    file2db,
    db2viz,
    csv2viz,
    json2viz)


# Read config.ini file
config_object = ConfigParser()
config_object.read('./settings/config.ini')
mysql_cred = config_object["MYSQL"]


class TestDataViz(unittest.TestCase):
    def setUp(self):

        # Get the user, the host, and the password from config.ini file
        self.user_mysql = mysql_cred["user"]
        self.host_mysql = mysql_cred["host"]
        self.password_mysql = mysql_cred["password"]
        self.filename_csv = "./tests/test_data/tmdb_results.csv"
        self.filename_json = "./tests/test_data/tmdb_page1.json"
        self.output_file_path = "./tests/test_result/"


class TestFile2Viz(TestDataViz):

    def test_csv2viz(self):
        """Test csv2viz() function"""

        try:
            # Visualize csv data
            csv2viz.csv2viz(self.filename_csv, kind="bar",
            y="popularity", x="title", title="TMDB Movies Popularity", labels={"y": "Popularity", "x": "Title"},
            update_trace_text=True, trace_text=None, file_path=self.output_file_path, show=True)
            self.assertTrue(os.path.isfile(r"{}/tmdb_movies_popularity.png".format(self.output_file_path)), True)

        except Exception as e:
            print('Error: {}'.format(str(e)))

    def test_json2viz(self):
        """Test json2viz() function"""

        try:
            # Visualize json data
            json2viz.json2viz(self.filename_json, key="results", kind="bar",
            y="popularity", x="title", title="TMDB Movies Popularity", labels={"y": "Popularity", "x": "Title"},
            update_trace_text=True, trace_text=None, file_path=self.output_file_path, show=True)
            self.assertTrue(os.path.isfile(r"{}/tmdb_movies_popularity.png".format(self.output_file_path)), True)

        except Exception as e:
            print('Error: {}'.format(str(e)))


class TestDB2Viz(TestDataViz):

    def test_db2viz(self):
        """Test db2viz() function"""

        try:
            # Create database tmdb
            file2db.file2db(self.host_mysql, self.user_mysql, self.password_mysql, self.filename_json, "tmdb", "tmdb_results", "json", "mysql", key="results")

            # Visualize data stored in database
            db2viz.db2viz(self.host_mysql, self.user_mysql, self.password_mysql, "tmdb", "tmdb_results", db_type="mysql", kind="bar",
            y="popularity", x="title", title="TMDB Movies Popularity", labels={"y": "Popularity", "x": "Title"},
            update_trace_text=True, trace_text=None, file_path=self.output_file_path,
            save2db=dict(host=self.host_mysql, user=self.user_mysql, password=self.password_mysql, db_type="mysql", db_name="tmdb", tb_name="image"),
            show=True)
            self.assertTrue(os.path.isfile(r"{}/tmdb_movies_popularity.png".format(self.output_file_path)), True)

        except Exception as e:
            print('Error: {}'.format(str(e)))


# Test Runner
if __name__ == '__main__':
    unittest.main()


# Database: titanic
# Table: titanic
# Table columns: ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare']


# Database: tmdb
# Table: tmdb_results
# Table columns: ['popularity', 'vote_count', 'poster_path', 'id', 'adult', 'backdrop_path', 'original_language', 'original_title', 'genre_ids', 'title', 'vote_average', 'overview', 'release_date', 'video']
