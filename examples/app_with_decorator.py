from flask import Flask
from flask_converter import Converter

app = Flask(__name__)

converter = Converter()
converter.init_app(app)

@converter.register('backwards')
def backwards(s):
    return s[::-1]

@app.route('/hi/')
def say_hi():
    return 'Hi there'

@app.route('/hello/<backwards:foo>/')
def hello_backwards(foo):
    return 'Hello %s' % (foo, )

if __name__ == '__main__':
    app.run()
