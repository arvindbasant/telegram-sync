from modals.telegram import Telegram
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    random_length = random.randrange(1, length)
    random_string = ''.join(random.choice(letters) for i in range(random_length)).upper()
    return random_string.ljust(length, ' ')


def get_random_number_string(length):
    numbers = "1234567890"
    random_length = random.randrange(1, length)
    random_number_string = ''.join(random.choice(numbers) for i in range(random_length))
    return random_number_string.ljust(length, ' ')


def get_telegram():
    telegram = Telegram(
        sender="EWM" + get_random_number_string(5),
        receiver=random.choice(["PRSCONF ", "PRSCONS "]),
        communication_point=get_random_string(18),
        handshake="R ",
        sequence_number=get_random_number_string(20),
        error=get_random_string(4),
        telegram_type=get_random_string(4),
        message_type=random.choice(["HUCFI", "HUCSI"]),
        warehouse_number=get_random_string(4),
        handling_unit_identification=get_random_string(20),
        material_number=get_random_string(18),
        batch=get_random_string(10),
        stock_type=get_random_string(2),
        order=get_random_string(12),
        status=random.choice(["Yes", "No "]),
        source_storage_bin=get_random_string(18),
        text1=get_random_string(8),
        text2=get_random_string(6),
        text3=get_random_string(12),
        text4=get_random_string(8),
        text5=get_random_string(40),
    )
    return telegram
