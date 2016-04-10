from werkzeug.routing import BaseConverter

class BackwardsConverter(BaseConverter):
    def to_python(self, value):
        return value[::-1]
    def to_url(self, value):
        return value[::-1]

class Converter(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        app.url_map.converters['backwards'] = BackwardsConverter
