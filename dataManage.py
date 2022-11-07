import json

def ReadData():
    with open("DB.json") as dataStorage:
        array = json.load(dataStorage)
    return array

def SaveData(data):
    with open("DB.json", "w", encoding = "utf-8") as dataStorage:
        dataStorage.write(json.dumps(data, ensure_ascii = False))
        dataStorage.close()