import logging
import pika
from services.rfid_response_service import RFIDResponseService

logger = logging.getLogger(__name__)

logging.getLogger("pika").setLevel(logging.WARNING)


def callback(ch, method, properties, body):
    RFIDResponseService(body).process_rfid_response()


connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('admin', 'Welcome1#'))
)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='telegram')  # Declare a queue
# set up subscription on the queue
channel.basic_consume('telegram',
                      callback,
                      auto_ack=True)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
