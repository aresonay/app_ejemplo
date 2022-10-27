from flask import Flask, make_response, abort, url_for

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return '<img src="'+url_for('static', filename='img/tux.png') + '"/>'


@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello', 200, headers)


@app.route('/login')
def login():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    return 'Página no encontrada', 404


@app.route('/hello')
@app.route('/hello/<string:name>')
def hello_name(name=None):
    return f'Hello {name}' if name else 'Hello whoever you are'




