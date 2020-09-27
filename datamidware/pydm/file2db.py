"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of file2db() function:
Imports raw structured/semi-structured data (csv, json) into db (MySQL, NoSQL).

param host: host name
param user: user name
param password: password
param filename: filename to send to pydb, str
param file_type: file type (csv, json, text, xml), str
param db_type: pydb type (mysql, nosql), str
param tb_name: name of the table where data will be stored, str

"""
# =================================================================
from __future__ import print_function
from .csv2mysql import csv2mysql
from .json2mysql import json2mysql


def file2db(host, user, password, filename, db_name, tb_name, file_type="csv", db_type="mysql", key=None):
    """
    Imports raw structured/semi-structured data (csv, json) into db (MySQL, NoSQL).

    :param host: host name
    :param user: user name
    :param password: password
    :param filename: filename to send to pydb
    :param file_type: file type (csv, json)
    :param db_type: pydb type (mysql, nosql)
    :param tb_name: name of the table where data will be stored
    :param key
    """

    if file_type == "csv":
        if db_type == "mysql":

            csv2mysql(host, user, password, filename=filename, db_name=db_name, tb_name=tb_name)

        if db_type == "nosql":
            pass

    if file_type == "json":
        if db_type == "mysql":
            json2mysql(host, user, password, filename=filename, db_name=db_name, tb_name=tb_name, key=key)

        if db_type == "nosql":
            pass

    if file_type == "xml":
        if db_type == "mysql":
            pass

        if db_type == "nosql":
            pass

    if file_type == "txt":
        if db_type == "mysql":
            pass

        if db_type == "nosql":
            pass

