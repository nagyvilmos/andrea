import json

# all default settings go in here, they can then be overwritten in the config.json file:

settings = {
    "databaseName": "test.db"
}

with open('config.json') as json_data:
    settings = json.load(json_data)
    print(settings)
