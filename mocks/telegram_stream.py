from mocks.telegram_builder import get_telegram_string
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.tcpclient import TCPClient
from tornado.options import options, define
import time

define("host", default="localhost", help="TCP server host")
define("port", default=9888, help="TCP port to connect to")


@gen.coroutine
def send_message():
    print('started telegram streaming....')
    stream = yield TCPClient().connect(options.host, options.port)
    for count in range(5):
        telegram = get_telegram_string() + '\n'
        yield stream.write(telegram.encode())
        time.sleep(2)


if __name__ == "__main__":
    options.parse_command_line()
    IOLoop.current().run_sync(send_message)
