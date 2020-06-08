import logging
import pika
from services.rfid_response_service import RFIDResponseService

logger = logging.getLogger(__name__)

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password'))
)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='telegram')  # Declare a queue


# create a function which is called on incoming messages


def callback(ch, method, properties, body):
    RFIDResponseService(body).process_rfid_response()


# set up subscription on the queue
channel.basic_consume('telegram',
                      callback,
                      auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()
