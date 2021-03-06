from flask import Flask, request, jsonify
import http.client
import json
from Recipe import Recipe
from Article import Article

app = Flask(__name__)

conn = http.client.HTTPSConnection("tasty.p.rapidapi.com")


@app.route('/')
def api_docs():
    return 'API Documentation goes here!'


@app.route('/apip1/search', methods=['POST'])
def search_recipe():
    search = request.get_json()

    conn.request("GET", "/recipes/list?from=0&size=10&q=" +
                 search['search'], headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    responce = dict()
    for i in range(len(data['results'])):
        recipe = data['results'][i]
        responce[i] = {'name': recipe['name'], 'tags': [],
                       'image': recipe['thumbnail_url'], 'id': recipe['id']}
        for j in recipe['tags']:
            responce[i]['tags'].append(j['name'])
    return jsonify(responce)


@app.route('/apip1/detail', methods=['POST'])
def recipe_detail():
    req = request.get_json()

    conn.request("GET", "/recipes/detail?id=" +
                 str(req['id']), headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    responce = Recipe(data)
    return jsonify(responce)


@app.route('/apip1/feed', methods=['POST'])
def feed():
    conn.request(
        "GET", "/feeds/list?size=20&timezone=%2B0700&vegetarian=false&from=0", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    responce = dict()
    responce['item'] = []
    for i in data['results']:
        if 'item' in i.keys():
            if 'recipes' in i['item'].keys():
                responce['item'].append(Article(i['item']))
            else:
                responce['item'].append(Recipe(i['item']))
        else:
            for article in i['items']:
                if 'recipes' in article.keys():
                    responce['item'].append(Article(article))
                else:
                    responce['item'].append(Recipe(article))
    return jsonify(responce)
