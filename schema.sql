CREATE TABLE RFID_RESPONSE
(
    ID                           INT PRIMARY KEY IDENTITY (1, 1),
    SENDER                       VARCHAR(8),
    RECEIVER                     VARCHAR(8),
    COMMUNICATION_POINT          VARCHAR(18),
    HANDSHAKE                    VARCHAR(2),
    SEQUENCE_NUMBER              VARCHAR(20),
    ERROR                        VARCHAR(4),
    TELEGRAM_TYPE                VARCHAR(4),
    MESSAGE_TYPE                 VARCHAR(5),
    WAREHOUSE_NUMBER             VARCHAR(4),
    HANDLING_UNIT_IDENTIFICATION VARCHAR(20),
    MATERIAL_NUMBER              VARCHAR(18),
    BATCH                        VARCHAR(10),
    STOCK_TYPE                   VARCHAR(2),
    TELEGRAM_ORDER               VARCHAR(12),
    TELEGRAM_STATUS              VARCHAR(3),
    SOURCE_STORAGE_BIN           VARCHAR(18),
    ERROR_MESSAGE                VARCHAR(74),
    RECEIVED_ON                  DATETIME,
);

CREATE PROCEDURE sp_delete_rfid_response
AS
BEGIN
    DELETE
    FROM RFID_RESPONSE
    WHERE DATEDIFF(DAY, RECEIVED_ON, GETDATE()) > 90
END