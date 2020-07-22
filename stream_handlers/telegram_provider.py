from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from modals.telegram import Telegram
from utils import logger
import logging
import os
import pika

logger = logger.get_logger(__name__)

rabbitmq_username = os.environ['RABBITMQ_USERNAME']
rabbitmq_password = os.environ['RABBITMQ_PASSWORD']
rabbitmq_queue_name = os.environ['RABBITMQ_QUEUE_NAME']
server_port = os.environ['SERVER_PORT']

logging.getLogger("pika").setLevel(logging.INFO)


class TelegramProvider(TCPServer):

    async def handle_stream(self, stream, address):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbitmq', 5672, '/',
                                      pika.PlainCredentials(rabbitmq_username, rabbitmq_password)))
        channel = connection.channel()
        channel.queue_declare(queue=rabbitmq_queue_name)
        while True:
            try:
                data = await stream.read_until(b"\n")
                channel.basic_publish(exchange='', routing_key=rabbitmq_queue_name, body=data)
                ack_telegram_str = Telegram.to_ack(data.decode().strip()).to_str() + "\n"
                await stream.write(ack_telegram_str.encode())
            except StreamClosedError:
                logger.warning("lost ewm connection, check ewm server..")
                connection.close()
                break
            except Exception as e:
                connection.close()
                logger.error("error %s", e)


if __name__ == "__main__":
    server = TelegramProvider()
    server.listen(int(server_port))
    logger.info("Listening on TCP port %s", server_port)
    IOLoop.current().start()
