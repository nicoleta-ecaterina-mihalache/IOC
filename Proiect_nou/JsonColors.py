import json

def read_colors():
    f = open('colors.json')

    data = json.load(f)
    #print(data)
    return data