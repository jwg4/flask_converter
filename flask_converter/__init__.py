from werkzeug.routing import BaseConverter

def make_converter(fn):
    class CustomConverter(BaseConverter):
        def to_python(self, value):
            return fn(value)
        def to_url(self, value):
            return value

    return CustomConverter

class Converter(object):
    def __init__(self, app=None, **kwargs):
        self.app = app
        self.converters = { k: make_converter(kwargs[k]) for k in kwargs }
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        for k in self.converters:
            app.url_map.converters[k] = self.converters[k]
