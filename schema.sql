CREATE TABLE RFID_RESPONSE
(
    ID                           INT PRIMARY KEY IDENTITY (1, 1),
    SENDER                       VARCHAR(8)  NOT NULL,
    RECEIVER                     VARCHAR(8)  NOT NULL,
    COMMUNICATION_POINT          VARCHAR(18) NOT NULL,
    HANDSHAKE                    VARCHAR(2)  NOT NULL,
    SEQUENCE_NUMBER              VARCHAR(20) NOT NULL,
    ERROR                        VARCHAR(4)  NOT NULL,
    TELEGRAM_TYPE                VARCHAR(4)  NOT NULL,
    MESSAGE_TYPE                 VARCHAR(5)  NOT NULL,
    WAREHOUSE_NUMBER             VARCHAR(4)  NOT NULL,
    HANDLING_UNIT_IDENTIFICATION VARCHAR(20) NOT NULL,
    MATERIAL_NUMBER              VARCHAR(18) NOT NULL,
    BATCH                        VARCHAR(10) NOT NULL,
    STOCK_TYPE                   VARCHAR(2)  NOT NULL,
    TELEGRAM_ORDER               VARCHAR(12) NOT NULL,
    TELEGRAM_STATUS              VARCHAR(3)  NOT NULL,
    SOURCE_STORAGE_BIN           VARCHAR(18) NOT NULL,
    ERROR_MESSAGE                VARCHAR(74) NOT NULL,
    RECEIVED_ON                  DATETIME    NOT NULL,
);