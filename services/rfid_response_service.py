from modals.telegram import Telegram
from repo.rfid_response_repo import insert_rfid_response, delete_90_days_older_response
from utils import logger

logger = logger.get_logger(__name__)


class RFIDResponseService:

    def __init__(self, payload):
        self.payload = payload

    def process_rfid_response(self):
        try:
            telegram_payload = self.payload.decode().strip()
            telegram_obj = Telegram.from_source(telegram_payload)
            insert_rfid_response(telegram_obj)
        except Exception as e:
            logger.error("error %s", e)

    @staticmethod
    def delete_rfid_response():
        try:
            delete_90_days_older_response()
        except Exception as e:
            logger.error("error %s", e)
