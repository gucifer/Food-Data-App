def get_nutrients(data):
    nutrients = dict()
    DailyNeeds = dict()
    set1 = data['bad']
    nutrient_list(set1, nutrients, DailyNeeds)
    set2 = data['good']
    nutrient_list(set2, nutrients, DailyNeeds)
    return [nutrients, DailyNeeds]


def nutrient_list(data, nutrients, DailyNeeds):
    for i in data:
        name = i['title']
        value = i['amount']
        parcent = i['percentOfDailyNeeds']
        nutrients[name] = value
        DailyNeeds[name] = parcent
