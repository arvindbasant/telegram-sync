from dataclasses import dataclass, asdict


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

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_source(cls, source):
        telegram = Telegram(
            sender=source[:8].replace('b', ''),
            receiver=source[8:16].replace('b', ''),
            communication_point=source[16:34].replace('b', ''),
            handshake=source[34:36].replace('b', ''),
            sequence_number=source[36:56].replace('b', ''),
            error=source[56:60].replace('b', ''),
            telegram_type=source[60:64].replace('b', ''),
            message_type=source[64:69].replace('b', ''),
            warehouse_number=source[69:73].replace('b', ''),
            handling_unit_identification=source[73:93].replace('b', ''),
            material_number=source[93:111].replace('b', ''),
            batch=source[111:121].replace('b', ''),
            stock_type=source[121:123].replace('b', ''),
            order=source[123:135].replace('b', ''),
            status=source[135:138].replace('b', ''),
            source_storage_bin=source[138:156].replace('b', ''),
            text1=source[156:164].replace('b', ''),
            text2=source[164:170].replace('b', ''),
            text3=source[170:182].replace('b', ''),
            text4=source[182:190].replace('b', ''),
            text5=source[190:230].replace('b', ''),
        )
        return telegram
