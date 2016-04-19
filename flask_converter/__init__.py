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
            self.init_app()
    
    def init_app(self, app):
        self.app = app
        self.register_all_known_converters()

    def register_all_known_converters(self):
        if self.app is not None:
            for k in self.converters:
                self.app.url_map.converters[k] = self.converters[k]

    def register(self, name):
        def register_function(fn):
            self.converters[name] = make_converter(fn)
            self.app.url_map.converters[name] = self.converters[name]
            return fn
        return register_function
