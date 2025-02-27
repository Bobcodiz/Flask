from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/<name>')
def hello_name(name):
    return f'Hello {escape(name)}'


if __name__ == '__main__':
    app.run(debug=True)
