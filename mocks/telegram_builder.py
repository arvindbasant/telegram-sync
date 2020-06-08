from modals.telegram import Telegram
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    random_length = random.randrange(1, length)
    random_string = ''.join(random.choice(letters) for i in range(random_length)).upper()
    return random_string.ljust(length, 'b')


def get_random_number_string(length):
    numbers = "1234567890"
    random_length = random.randrange(1, length)
    random_number_string = ''.join(random.choice(numbers) for i in range(random_length))
    return random_number_string.ljust(length, 'b')


def get_telegram():
    telegram = Telegram(
        sender=get_random_string(8),
        receiver=get_random_string(8),
        communication_point=get_random_string(18),
        handshake=get_random_string(2),
        sequence_number=get_random_number_string(20),
        error=get_random_string(4),
        telegram_type=get_random_string(4),
        message_type=get_random_string(5),
        warehouse_number=get_random_string(4),
        handling_unit_identification=get_random_string(20),
        material_number=get_random_string(18),
        batch=get_random_string(10),
        stock_type=get_random_string(2),
        order=get_random_string(12),
        status=get_random_string(3),
        source_storage_bin=get_random_string(18),
        text1=get_random_string(8),
        text2=get_random_string(6),
        text3=get_random_string(12),
        text4=get_random_string(8),
        text5=get_random_string(40),
    )
    return telegram


def get_telegram_string():
    telegram = get_telegram()
    return telegram.sender + telegram.receiver + telegram.communication_point + telegram.handshake \
           + telegram.sequence_number + telegram.error + telegram.telegram_type + telegram.message_type \
           + telegram.warehouse_number + telegram.handling_unit_identification + telegram.material_number \
           + telegram.batch + telegram.stock_type + telegram.order + telegram.status \
           + telegram.source_storage_bin + telegram.text1 + telegram.text2 + telegram.text3 \
           + telegram.text4 + telegram.text5
