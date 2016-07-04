import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.platform.twisted

tornado.platform.twisted.install()

from twisted.web.xmlrpc import Proxy
from twisted.internet import reactor

proxy = Proxy('http://advogato.org/XMLRPC')

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def printValue(self, value):
        self.write(repr(value))
        self.finish()

    def printError(self, error):
        self.write('error: %s' % error) 
        self.finish()

    @tornado.web.asynchronous
    def get(self):
        proxy.callRemote('test.sumprod', 3, 5).addCallbacks(self.printValue, self.printError)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()