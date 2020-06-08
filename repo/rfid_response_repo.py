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
    INSERT INTO telegramdb.dbo.RFID_RESPONSE(sender, receiver, communication_point, handshake, sequence_number, error, 
    telegram_type, message_type, warehouse_number, handling_unit_identification, material_number, batch, stock_type, 
    telegram_order, telegram_status, source_storage_bin, text1, text2, text3, text4, text5, received_on)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )""",
                   telegram.sender, telegram.receiver, telegram.communication_point, telegram.handshake,
                   telegram.sequence_number, telegram.error, telegram.telegram_type, telegram.message_type,
                   telegram.warehouse_number, telegram.handling_unit_identification, telegram.material_number,
                   telegram.batch, telegram.stock_type, telegram.order, telegram.status,
                   telegram.source_storage_bin, telegram.text1, telegram.text2, telegram.text3, telegram.text4,
                   telegram.text5, datetime.datetime.now())
    conn.commit()
