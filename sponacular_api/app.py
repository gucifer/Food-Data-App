from flask import Flask, request, jsonify
import http.client
import json

app = Flask(__name__)
conn = http.client.HTTPSConnection("api.spoonacular.com")

API_KEY = "26ffc548096f45d09e84bbff675aa992"


@app.route('/')
def index():
    return 'Hello World'


@app.route('/api/search', methods=['POST'])
def search_recipe():
    req = request.get_json()

    search = req['search']
    conn.request("GET", "/recipes/complexSearch?apiKey="+API_KEY+"&number=10")
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode('utf-8'))
    print(data)
    responce = dict()
    responce['recipes'] = data['results']
    responce['totalResults'] = data['totalResults']
    return jsonify(responce)


@app.route('/api/recipedetail',methods=['POST'])
def recipe_detail():
    

@app.route('/api/search/advanced')
def advanced_search():
    return


@app.route('/api/recipe')
def get_recipe():
    req = request.get_json()

    return
