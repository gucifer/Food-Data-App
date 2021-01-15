from flask import Flask, request, jsonify
import http.client
import json
from ingredients import get_ingredients
from wines import get_wine
from steps import get_steps
from nutrients import get_nutrients

app = Flask(__name__)
conn = http.client.HTTPSConnection("api.spoonacular.com")


def dict_check(key, d):
    if key in d.keys():
        return True
    return False


def get_tags(data):
    responce = dict()
    responce["vegetarian"] = data["vegetarian"]
    responce["vegan"] = data["vegan"]
    responce["glutenFree"] = data["glutenFree"]
    responce["dairyFree"] = data["dairyFree"]
    responce["veryHealthy"] = data["veryHealthy"]
    responce["cheap"] = data["cheap"]
    responce["veryPopular"] = data["veryPopular"]
    responce["sustainable"] = data["sustainable"]
    return responce


def get_data():
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode('utf-8'))
    return data


@app.route('/')
def index():
    return 'Hello World'


@app.route('/api/search', methods=['POST'])
def search_recipe():
    req = request.get_json()
    search = req['search']
    conn.request("GET", "/recipes/complexSearch?apiKey=" +
                 API_KEY+"&number=10&query="+search)
    data = get_data()

    responce = dict()
    responce['recipes'] = data['results']
    responce['totalResults'] = data['totalResults']
    return jsonify(responce)


@app.route('/api/search/advanced')
def advanced_search():
    return NotImplementedError


@app.route('/api/recipe/detail', methods=['POST'])
def recipe_detail():
    req = request.get_json()
    search = req['id']
    conn.request('GET', '/recipes/'+str(search)+'/information?apiKey='+API_KEY)
    data = get_data()

    responce = dict()
    responce['name'] = data['title']
    responce['tags'] = get_tags(data)
    responce['ingredients'] = get_ingredients(data)
    responce['image'] = data['image']
    responce['summary'] = data['summary']
    if 'winePairing' in data.keys():
        responce['wine'] = get_wine(data)
    return responce


@app.route('/api/recipe/instructions', methods=['POST'])
def recipe_instruction():
    req = request.get_json()
    search = req['id']
    conn.request('GET', '/recipes/'+str(search) +
                 '/analyzedInstructions?apiKey='+API_KEY)
    data = get_data()

    responce = get_steps(data)

    return jsonify(responce)


@app.route('/api/recipe/nutrients', methods=['POST'])
def recipe_nutrients():
    req = request.get_json()
    search = req['id']
    conn.request('GET', '/recipes/'+str(search) +
                 '/nutritionWidget.json?apiKey='+API_KEY)
    data = get_data()

    responce = get_nutrients(data)
    return jsonify(responce)


@app.route('/api/random', methods=['POST'])
def random_recipe():
    conn.request('GET', '/recipes/random?number=1&apiKey='+API_KEY)
    data = get_data()
    return data
