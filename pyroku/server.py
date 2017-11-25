from flask import Flask, Response
from os import environ
from json import dumps as json_dumps

app = Flask(__name__)


@app.route('/')
def root():
    return Response(json_dumps({"test": "value"}), mimetype='application/json')


if __name__ == '__main__':
    app.run('0.0.0.0', int(environ.get('SERVER_PORT') or 8080))
