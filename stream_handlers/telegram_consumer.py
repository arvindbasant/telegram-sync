import logging
import pika
import os
from services.rfid_response_service import RFIDResponseService

logger = logging.getLogger(__name__)
rabbitmq_username = os.environ['RABBITMQ_USERNAME']
rabbitmq_password = os.environ['RABBITMQ_PASSWORD']
rabbitmq_queue_name = os.environ['RABBITMQ_QUEUE_NAME']

logging.getLogger("pika").setLevel(logging.WARNING)


def callback(ch, method, properties, body):
    RFIDResponseService(body).process_rfid_response()


connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials(rabbitmq_username, rabbitmq_password))
)
# start a channel
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue=rabbitmq_queue_name)

# set up subscription on the queue
channel.basic_consume(rabbitmq_queue_name,
                      callback,
                      auto_ack=True)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
