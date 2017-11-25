from flask import Flask, Response
from os import environ
from json import dumps as json_dumps
from pyroku.roku import get_roku_ids, roku_key

app = Flask(__name__)


@app.route('/roku')
def roku_list():
    return Response(json_dumps(get_roku_ids()), mimetype='application/json')


@app.route('/roku/<roku_id>/key/<key_id>')
def key(roku_id, key_id):
    return Response(json_dumps(roku_key(roku_id, key_id)), mimetype='application/json')


@app.route('/')
def root():
    return Response(json_dumps({'root': 'root'}), mimetype='application/json')


if __name__ == '__main__':
    app.run('0.0.0.0', int(environ.get('SERVER_PORT') or 8080))
