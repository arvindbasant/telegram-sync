from mocks.telegram_builder import get_telegram
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.options import options, define
import time
import logging

define("host", default="127.0.0.1", help="TCP server host")
define("port", default=52004, help="TCP port to connect to")
logger = logging.getLogger(__name__)


async def stream_telegram():
    stream = await TCPClient().connect(options.host, options.port)
    for count in range(5):
        telegram = get_telegram().to_str() + '\n'
        await stream.write(telegram.encode())
        reply = await stream.read_until(b"\n")
        logger.info("Acknowledgement Received %s", reply.decode().strip())
        time.sleep(2)


if __name__ == "__main__":
    options.parse_command_line()
    IOLoop.current().run_sync(stream_telegram)
