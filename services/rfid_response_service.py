from modals.telegram import Telegram
from repo.rfid_response_repo import insert_rfid_response


class RFIDResponseService:

    def __init__(self, payload):
        self.payload = payload

    def process_rfid_response(self):
        telegram_payload = self.payload.decode().strip()
        telegram_obj = Telegram.from_source(telegram_payload)
        insert_rfid_response(telegram_obj)
