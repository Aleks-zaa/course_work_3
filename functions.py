import json

def load_data(file):
    '''Функция из JSON в Python для загрузки данных из файла.'''
    with open(file, encoding="utf-8") as f:
        data = json.load(f)
        return data


