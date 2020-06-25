import pyodbc
import os


def connect():
    mssql_server = os.environ['MSSQL_SERVER']
    mssql_port = os.environ['MSSQL_PORT']
    mssql_database = os.environ['MSSQL_DATABASE']
    mssql_username = os.environ['MSSQL_USERNAME']
    mssql_password = os.environ['MSSQL_PASSWORD']

    driver = '/usr/lib/libtdsodbc.so'
    try:
        conn = pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + mssql_server + ';PORT=' + mssql_port + ';DATABASE=' + mssql_database + ';UID=' + mssql_username + ';PWD=' + mssql_password + '')
    except Exception as e:
        print(f"Database connection error: {e}")
    else:
        cursor = conn.cursor()
        return conn, cursor
