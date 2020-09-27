"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
=======================================================================================
Implementation of db2file() function:
Exports table data as csv/json format from the pydb

param host: host name
param user: user name
param password: password
param file_path: file path to export data from pydb
param file_type: file type (csv, json)
param db_type: pydb type (mysql, nosql)
param db_name: pydb name from where data is exported
param tb_name: name of the table from where data will be exported

"""
# =====================================================================================
from __future__ import print_function
from .mysql2csv import mysql2csv


def db2file(host, user, password, file_path, db_name, tb_name, file_type="csv", db_type="mysql"):
    """

    :param host: host name
    :param user: user name
    :param password: password
    :param file_path: file path to export data from pydb
    :param file_type: file type (csv, json)
    :param db_type: pydb type (mysql, nosql)
    :param db_name: the name of the pydb
    :param tb_name: name of the table from where data will be exported
    """

    if file_type == "csv":
        if db_type == "mysql":

            mysql2csv(host, user, password, file_path=file_path, db_name=db_name, tb_name=tb_name)

        if db_type == "nosql":
            pass

    if file_type == "json":
        if db_type == "mysql":
            mysql2csv(host, user, password, file_path=file_path, db_name=db_name, tb_name=tb_name)

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


