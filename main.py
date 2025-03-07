from flask import Flask
from markupsafe import escape

# flask --app main  --debug run

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Home</h1>'


@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name=None, age=None):
    if name is not None and age is not None:
        return f'hello {name} your age is {age}'

    return 'hello'


# http://127.0.0.1:5000/code/<script>alert('test')</script>
@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
