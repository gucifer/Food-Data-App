from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/api/search')
def search_recipe():
    req = request.get_json()
    responce = dict()
    responce = req
    return jsonify(responce)
