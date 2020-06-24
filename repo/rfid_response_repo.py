import pyodbc
import datetime


def pyodbc_localhost():
    driver = '/usr/lib/libtdsodbc.so'  # NOT THE MOST ELEGANT WAY, BUT WE'RE TELLING PYODBC WHERE TO FIND THE FREETDS DRIVER
    try:
        conn = pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=172.17.0.2;PORT=1433;DATABASE=telegramdb;UID=sa;PWD=Pass*123')
    except Exception as e:
        print(f"Couldn't connect to db on localhost because {e}")
    else:
        cursor = conn.cursor()
        return conn, cursor


def insert_rfid_response(telegram):
    # driver = '/usr/lib/libtdsodbc.so'
    # conn_str = (
    #     r'DRIVER={' + driver + '};'
    #     r'SERVER=172.17.0.2,1433;'
    #     r'DATABASE=telegramdb;'
    #     r'UID=sa;'
    #     r'PWD=Pass*123;'
    # )
    #
    # conn = pyodbc.connect(conn_str)
    # cursor = conn.cursor()

    print("trying to insert")

    conn, cursor = pyodbc_localhost()

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
