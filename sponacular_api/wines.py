def get_wine(data):
    wines = data['winePairing']
    responce = dict()
    if 'apiredWines' in wines.keys():
        responce['wines'] = wines['pairedWines']
    if 'pairingText' in wines.keys():
        responce['text'] = wines['pairingText']
    return responce
