"""
Implementation of db2viz() function:
Visualize database data

param host: host name
param user: user name
param password: password
param db_type: database type (mysql, nosql)
param db_name: database name
param tb_name: name of the table
param kind: plot kind (bar, horizontal bar, stacked bar, group bar, scatter, line, hist,
                       kde, pie and more..)
param file_path: file path to save figure
param x: x data; list or array-like data
param y: y data; list or array-like data
param title: title of the figure
param label: x-label, y-label
param show: If True, show the current figure; default=True
"""
# =====================================================================================
from __future__ import print_function
import pandas as pd
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from datamidware.pyviz import bar
import mysql.connector
from mysql.connector import errorcode


def db2viz(host, user, password, db_name, tb_name, db_type=None, kind=None, x=None, y=None,
           xcol_pos=None, ycol_pos=None, color=None, title=None, labels={}, set_col_color=None,
           update_title={}, update_xaxes={}, update_yaxes={}, xtickangle=None, ytickangle=None,
           xtickformat=None, ytickformat=None, update_legend={}, update_font={}, hover_name=None,
           hover_data=None, barmode="relative", bargap=0.15, bargroupgap=0.1, color_discrete_sequence=None,
           fig_width=1200, fig_height=800, color_continuous_scale=None, plot_bgcolor="rgba(0, 0, 0, 0)",
           paper_bgcolor="rgba(0, 0, 0, 0)", uniformtext_minsize=8, uniformtext_mode="hide",
           marker={}, selector={}, trace_name=None, update_trace_text=False, trace_text=None,
           texttemplate='%{text:.2s}', textangle=None, textposition="outside",textfont={}, bar_width=None,
           hoverinfo=None, hoverlabel=None, hovertemplate=None, hovertext=None,
           sort_asc=False, sort_desc=False, N_largest=None, N_smallest=None,
           file_path=None, save2db={}, file_type="png", show=True):
    """

    :param host:
    :param user:
    :param password:
    :param db_name:
    :param tb_name:
    :param db_type:
    :param kind:
    :param x:
    :param y:
    :param xcol_pos:
    :param ycol_pos:
    :param color:
    :param title:
    :param labels:
    :param set_col_color:
    :param update_title:
    :param update_xaxes:
    :param update_yaxes:
    :param xtickangle:
    :param ytickangle:
    :param xtickformat:
    :param ytickformat:
    :param update_legend:
    :param update_font:
    :param hover_name:
    :param hover_data:
    :param barmode:
    :param bargap:
    :param bargroupgap:
    :param color_discrete_sequence:
    :param fig_width:
    :param fig_height:
    :param color_continuous_scale:
    :param plot_bgcolor:
    :param paper_bgcolor:
    :param uniformtext_minsize:
    :param uniformtext_mode:
    :param marker:
    :param selector:
    :param trace_name:
    :param update_trace_text:
    :param trace_text:
    :param texttemplate:
    :param textangle:
    :param textposition:
    :param textfont:
    :param bar_width:
    :param hoverinfo:
    :param hoverlabel:
    :param hovertemplate:
    :param hovertext:
    :param sort_asc:
    :param sort_desc:
    :param N_largest:
    :param N_smallest:
    :param file_path:
    :param save2db: dict(host="hostname", user = "user",
                         password = "password", db_name = "db_name",
                         tb_name = "tb_name")
    :param file_type:
    :param show:
    :return:
    """



    try:
        plot = bar.BarChart()
        if db_type == "mysql":
            # if db "db_name" exits
            if exists_db(host, user, password, db_name=db_name):

                # if table already exists
                if exists_tb(host, user, password, db_name=db_name, tb_name=tb_name):

                    # get the table data into pandas dataframe
                    df = mysql2df(host, user, password, db_name, tb_name)

                    # remove all whitespaces in the columns
                    df.columns = df.columns.str.replace(' ', '')

                    # plot bar chart
                    if kind == "bar":
                        plot.bar(df=df, x=x, y=y, xcol_pos=xcol_pos, ycol_pos=ycol_pos, color=color, title=title, labels=labels,
                                         set_col_color=set_col_color, update_title=update_title, update_xaxes=update_xaxes, update_yaxes=update_yaxes,
                                         xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat, ytickformat=ytickformat,
                                         update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                                         hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                                         color_discrete_sequence=color_discrete_sequence, fig_width=fig_width, fig_height=fig_height,
                                         color_continuous_scale=color_continuous_scale, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                                         uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode,
                                         marker=marker, selector=selector, trace_name=trace_name, update_trace_text=update_trace_text,
                                         trace_text=trace_text, texttemplate=texttemplate, textangle=textangle, textposition=textposition,
                                         textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo, hoverlabel=hoverlabel, hovertemplate=hovertemplate,
                                         hovertext=hovertext, sort_asc=sort_asc, sort_desc=sort_desc,
                                         N_largest=N_largest, N_smallest=N_smallest, file_path=file_path, save2db=save2db, file_type=file_type, show=show)

                    # plot horizontal bar chart
                    if kind == "barh":
                        plot.barh(df=df, x=x, y=y, xcol_pos=xcol_pos, ycol_pos=ycol_pos, color=color, title=title, orientation="h", labels=labels,
                                         set_col_color=set_col_color, update_title=update_title, update_xaxes=update_xaxes, update_yaxes=update_yaxes,
                                         xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat, ytickformat=ytickformat,
                                         update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                                         hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                                         color_discrete_sequence=color_discrete_sequence, fig_width=fig_width, fig_height=fig_height,
                                         color_continuous_scale=color_continuous_scale, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                                         uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode,
                                         marker=marker, selector=selector, trace_name=trace_name, update_trace_text=update_trace_text,
                                         trace_text=trace_text, texttemplate=texttemplate, textangle=textangle, textposition=textposition,
                                         textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo, hoverlabel=hoverlabel, hovertemplate=hovertemplate,
                                         hovertext=hovertext, sort_asc=sort_asc, sort_desc=sort_desc, N_largest=N_largest,
                                         N_smallest=N_smallest, file_path=file_path, save2db=save2db, file_type=file_type, show=show)

                    if kind == "line":
                        pass

                    if kind == "scatter":
                        pass

                    if kind == "hist":
                        pass

                    if kind == "kde":
                        pass

                    if kind == "box":
                        pass

                    if kind == "pie":
                        pass

                # if table does not exist, raise error
                else:

                    raise ImportError("table {} does not exist.".format(tb_name))

            # if db does not exist, raise error
            else:
                raise ImportError("db {} does not exist.".format(db_name))

        if db_type == "nosql":
            pass

    except Exception as e:
        print('Error: {}'.format(str(e)))


# ====================================================================
# Checks if given db and table already exists or not

# param host: host name
# param user: user name
# param password: password
# param db_name: filename to send to pydb
# param tb_name: name of the table where data will be stored
# ====================================================================


# Checks if given pydb already exists or not
def exists_db(host, user, password, db_name):
    """
    Return True if pydb exists, else return False.

    :param host: host
    :param user: user
    :param password: password
    :param db_name: pydb name to check if exists or not
    :return: True if exists, else return False
    """
    # Create a connection object
    connection = mysql.connector.connect(host=host,
                                 user=user,
                                 password=password)

    connection.autocommit = True

    # Create a cursor object
    cursor = connection.cursor()

    # check if pydb exists
    sql_query = "SHOW DATABASES"
    cursor.execute(sql_query)

    for db in cursor:
        # print(db.values())
        for val in db.values():
            if val == db_name:
                return True

    return False


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
    connection = mysql.connector.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=db_name)

    connection.autocommit = True

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


def mysql2df(host, user, password, db_name, tb_name):
    """
    Return mysql table data as pandas DataFrame.

    :param host: host name
    :param user: user name
    :param password: password
    :param db_name: name of the pydb from where data will be exported
    :param tb_name: name of the table from where data will be exported
    """

    # Create a connection object
    # dialect+driver://username:password@host:port/pydb
    connect_string = "mysql+pymysql://{}:{}@{}/{}".format(user, password, host, db_name)
    engine = db.create_engine(connect_string, encoding='latin1', echo=True, pool_pre_ping=True)
    connection = engine.connect()
    session = sessionmaker(bind=engine)()
    metadata = db.MetaData()

    try:
        # print the table column names
        tb = db.Table(tb_name, metadata, autoload=True, autoload_with=engine)
        print(tb.columns.keys())

        # Retrieve table data: 'SELECT * FROM table'
        sql_query = 'SELECT * FROM {}'.format(tb_name)
        df = pd.read_sql(sql_query, connection)
        return df

    except Exception as e:
        print('Error: {}'.format(str(e)))

    finally:
        engine.dispose()
        session.close()


