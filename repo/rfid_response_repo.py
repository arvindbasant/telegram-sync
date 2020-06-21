import pyodbc
import datetime


def insert_rfid_response(telegram):
    conn_str = (
        r'Driver={ODBC Driver 17 for SQL Server};'
        r'Server=127.0.0.1,1433;'
        r'Database=telegramdb;'
        # r'Trusted_Connection=Yes;'
        r'UID=sa;'
        r'PWD=Pass*123;'
    )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

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
