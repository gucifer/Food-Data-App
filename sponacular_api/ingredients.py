def get_ingredients(data):
    ingredients = data['extendedIngredients']
    responce = list()
    for i in ingredients:
        ing = dict()
        ing['name'] = i['name']
        ing['orig'] = i['original']
        ing['image'] = 'https://spoonacular.com/cdn/ingredients_100x100/'+i['image']
        responce.append(ing)
    return responce
