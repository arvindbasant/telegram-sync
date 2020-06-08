import logging
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.options import options, define

import pika

define("port", default=9888, help="TCP port to listen on")
logger = logging.getLogger(__name__)


class TelegramProvider(TCPServer):

    async def handle_stream(self, stream, address):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
        channel = connection.channel()
        channel.queue_declare(queue='telegram')
        while True:
            try:
                data = await stream.read_until(b"\n")
                channel.basic_publish(exchange='', routing_key='telegram', body=data)
                logger.info("Received: %s", data.decode().strip())
            except StreamClosedError:
                logger.warning("Lost client at host %s", address[0])
                connection.close()
                break
            except Exception as e:
                connection.close()
                print("error %s", e)


if __name__ == "__main__":
    options.parse_command_line()
    server = TelegramProvider()
    server.listen(options.port)
    logger.info("Listening on TCP port %d", options.port)
    IOLoop.current().start()
