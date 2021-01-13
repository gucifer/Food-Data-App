def get_steps(data):
    responce = []
    for item in data:
        d = dict()
        d['name'] = item['name']
        steps = item['steps']
        d['steps'] = parse_steps(steps)
        responce.append(d)
    return responce


def parse_steps(steps):
    responce = []
    for step in steps:
        responce.append(step['step'])
    return responce
