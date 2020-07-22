import pyodbc
import os
from utils import logger

logger = logger.get_logger(__name__)


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
        logger.error("Database Connection error %s", e)
    else:
        cursor = conn.cursor()
        return conn, cursor
