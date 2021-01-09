def Recipe(data):
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
        responce['tags'].append({'name': i['name'], 'type': i['type']})
    responce['instructions'] = []
    for i in data['instructions']:
        responce['instructions'].append(i['display_text'])
    responce['image'] = data['thumbnail_url']
    return responce
