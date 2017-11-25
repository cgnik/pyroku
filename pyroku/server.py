from flask import Flask, send_from_directory
from os import environ

app = Flask(__name__)


@app.route('/')
def root():
    return send_from_directory('public', 'index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', int(environ.get('SERVER_PORT') or 8080))
