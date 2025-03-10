from datetime import datetime
from flask import Flask, render_template, request
from markupsafe import escape

# flask --app main  --debug run

app = Flask(__name__)


# app.add_template_filter(format_date, 'format_date') => instead of @app.add_template_filter
# app.add_template_global(repeat, 'repeat') => instead of @app.add_template_global


# Filters

@app.add_template_filter
def format_date(date):
    return date.strftime('%d-%m-%Y')


# End filters

@app.add_template_global
def repeat(s, n):
    return s * n


# Routes
@app.route('/')
def index():
    date = datetime.now()
    name = 'David'
    friends = ['Daniel', 'Veronica', 'Fernando']
    # return '<h1>Home</h1>'
    return render_template('index.html', name=name, friends=friends, date=date)  # , repeat=repeat


@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name=None, age=None):
    return render_template('hello.html', name=name, age=age)


# if name is not None and age is not None:
#        return f'hello {name} your age is {age}'

#   return 'hello'


# http://127.0.0.1:5000/code/<script>alert('test')</script>
@app.route('/code/<path:code>')
def code(c):
    return f'<code>{escape(c)}</code>'


@app.route('/auth/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return render_template('/auth/register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) < 6 or len(password) < 6:
            error = """Username length must be greater than 6,
            Password length must be greater than 6
            """
            return render_template('/auth/register.html', error=error)
