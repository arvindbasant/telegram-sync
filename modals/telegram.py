from dataclasses import dataclass


@dataclass(frozen=True)
class Telegram:
    sender: str
    receiver: str
    communication_point: str
    handshake: str
    sequence_number: str
    error: str
    telegram_type: str
    message_type: str
    warehouse_number: str
    handling_unit_identification: str
    material_number: str
    batch: str
    stock_type: str
    order: str
    status: str
    source_storage_bin: str
    text1: str
    text2: str
    text3: str
    text4: str
    text5: str

    @classmethod
    def from_source(cls, source):
        telegram = Telegram(
            sender=source[:8],
            receiver=source[8:16],
            communication_point=source[16:34],
            handshake=source[34:36],
            sequence_number=source[36:56],
            error=source[56:60],
            telegram_type=source[60:64],
            message_type=source[64:69],
            warehouse_number=source[69:73],
            handling_unit_identification=source[73:93],
            material_number=source[93:111],
            batch=source[111:121],
            stock_type=source[121:123],
            order=source[123:135],
            status=source[135:138],
            source_storage_bin=source[138:156],
            text1=source[156:164],
            text2=source[164:170],
            text3=source[170:182],
            text4=source[182:190],
            text5=source[190:230],
        )
        return telegram

    @classmethod
    def to_ack(cls, source):
        sender = source[:8]
        receiver = source[8:16]
        telegram = Telegram(
            sender=receiver,
            receiver=sender,
            communication_point=source[16:34],
            handshake="C ",
            sequence_number=source[36:56],
            error=source[56:60],
            telegram_type=source[60:64],
            message_type=source[64:69],
            warehouse_number=source[69:73],
            handling_unit_identification=source[73:93],
            material_number=source[93:111],
            batch=source[111:121],
            stock_type=source[121:123],
            order=source[123:135],
            status=source[135:138],
            source_storage_bin=source[138:156],
            text1=source[156:164],
            text2=source[164:170],
            text3=source[170:182],
            text4=source[182:190],
            text5=source[190:230],
        )
        return telegram

    def to_str(self):
        return self.sender + self.receiver + self.communication_point + self.handshake \
               + self.sequence_number + self.error + self.telegram_type + self.message_type \
               + self.warehouse_number + self.handling_unit_identification + self.material_number \
               + self.batch + self.stock_type + self.order + self.status \
               + self.source_storage_bin + self.text1 + self.text2 + self.text3 \
               + self.text4 + self.text5
