from flask import Flask, request, jsonify
import http.client
import json
import pickle

app = Flask(__name__)
headers = {
    'x-rapidapi-key': "36f705baa8msh44335f3142fd8fdp166372jsn51f840150135",
    'x-rapidapi-host': "tasty.p.rapidapi.com"
}

@app.route('/')
def api_docs():
    return 'API Documentation goes here!'


@app.route('/api/search', methods=['POST'])
def search_recipe():
    search = request.get_json()
    conn = http.client.HTTPSConnection("tasty.p.rapidapi.com")
    conn.request("GET", "/recipes/list?from=0&size=10&q=" + search['search'], headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    
    responce = dict()
    for i in range(len(data['results'])):
        recipe = data['results'][i]
        responce[i] = {'name': recipe['name'],'tags': [],'image':recipe['thumbnail_url'],'id': recipe['id']}
        for j in recipe['tags']:
            responce[i]['tags'].append(j['name'])
    return jsonify(responce)


@app.route('/api/detail', methods=['POST'])
def recipe_detail():
    req = request.get_json()
    
    conn = http.client.HTTPSConnection("tasty.p.rapidapi.com")
    conn.request("GET", "/recipes/detail?id=" + str(req['id']), headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    
    responce = dict()
    responce['id'] = data['id']
    if 'yields' in data.keys():
        responce['servings'] = data['yields']
    responce['ease'] = data['recirc_feeds']['ease']
    responce['meal'] = data['recirc_feeds']['ease']
    responce['video'] = data['original_video_url']
    responce['nutrition'] = data['nutrition']
    responce['tags'] = []
    for i in data['tags']:
        responce['tags'].append({'name':i['name'],'type':i['type']})
    responce['instructions'] = []
    for i in data['instructions']:
        responce['instructions'].append(i['display_text'])
    responce['image'] = data['thumbnail_url']
    return jsonify(responce)

@app.route('/api/feed', methods=['POST'])
def feed(): 
    conn = http.client.HTTPSConnection("tasty.p.rapidapi.com")
    conn.request("GET", "/feeds/list?size=20&timezone=%2B0700&vegetarian=false&from=0", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    
    responce = dict()
    feed_list = data['results']
    n = len(feed_list)
    return
