import tornado.ioloop
from tornado.options import options
import tornado.platform.caresresolver


from .version import version
from .app import make_app

from .options import *

__version__ = version


if __name__ == '__main__':
    tornado.options.parse_command_line()
    tornado.options.parse_config_file(options.config)
    tornado.options.parse_command_line()

    app = make_app()
    app.listen(options.port, options.host)
    tornado.ioloop.IOLoop.current().start()
