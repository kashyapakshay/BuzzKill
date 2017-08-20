import tornado.ioloop
import tornado.web

from classifier import Classifier

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Clickbait Classifier: Make POST request to /classify with text to classify.')

class ClassificationHandler(tornado.web.RequestHandler):
    def initialize(self, classifier):
        self.classifier = classifier

    def _is_clickbait(self, text):
        return bool(self.classifier.classify(text))

    def get(self, text):
        self.write(str(self._is_clickbait(text)))

    def post(self):
        self.write(str(self._is_clickbait(text)))

def make_app():
    classifier = Classifier()

    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/classify/(\w+)', ClassificationHandler, dict(classifier=classifier))
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
