import json


def read_credentials():
    with open('data.json') as f:
        data = json.load(f)
    return data['valid'], data['invalid']