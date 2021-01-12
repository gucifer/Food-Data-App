from Recipe import Recipe
def Article(article):
    responce = dict()
    responce['name'] = article['name']
    responce['image'] = article['thumbnail_url']
    responce['video'] = article['video_url']
    responce['recipes'] = list()
    responce['tags'] = []
    for j in article['tags']:
        responce['tags'].append(j['display_name'])
    for recipe in article['recipes']:
        responce['recipes'].append(Recipe(recipe))
    return responce