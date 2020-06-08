from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options


def define_options():
    define("port", default=8888, help="run on given port", type=int)


class FeedbackApplication(Application):
    def __init__(self):
        handlers = get_urls()
        Application.__init__(self, handlers, debug=True)


def main():
    define_options()
    options.parse_command_line()
    http_server = HTTPServer(FeedbackApplication())
    http_server.listen(options.port)
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
