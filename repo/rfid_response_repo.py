import pyodbc
import datetime
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


def insert_rfid_response(telegram):
    conn, cursor = connect()
    cursor.execute("""
    INSERT INTO telegramdb.dbo.RFID_RESPONSE(SENDER, RECEIVER, COMMUNICATION_POINT, HANDSHAKE, SEQUENCE_NUMBER, ERROR, 
    TELEGRAM_TYPE, MESSAGE_TYPE, WAREHOUSE_NUMBER, HANDLING_UNIT_IDENTIFICATION, MATERIAL_NUMBER, BATCH, STOCK_TYPE, 
    TELEGRAM_ORDER, TELEGRAM_STATUS, SOURCE_STORAGE_BIN, ERROR_MESSAGE, RECEIVED_ON)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )""",
                   telegram.sender.rstrip(),
                   telegram.receiver.rstrip(),
                   telegram.communication_point.rstrip(),
                   telegram.handshake.rstrip(),
                   telegram.sequence_number.rstrip(),
                   telegram.error.rstrip(),
                   telegram.telegram_type.rstrip(),
                   telegram.message_type.rstrip(),
                   telegram.warehouse_number.rstrip(),
                   telegram.handling_unit_identification.rstrip(),
                   telegram.material_number.rstrip(),
                   telegram.batch.rstrip(),
                   telegram.stock_type.rstrip(),
                   telegram.order.rstrip(),
                   telegram.status.rstrip(),
                   telegram.source_storage_bin.rstrip(),
                   (telegram.text1 + telegram.text2 + telegram.text3 + telegram.text4 + telegram.text5).rstrip(),
                   datetime.datetime.now())
    conn.commit()
