import json
from datetime import datetime, date


def load_data(file):
    """Функция из JSON в Python для загрузки данных из файла."""
    with open(file, encoding="utf-8") as f:
        data = json.load(f)
        return data


def sort_status(file):
    """Сортируем по статусу"""
    return [x for x in file if x['state'] == 'EXECUTED']


def sort_data(data):
    """Сортируем по дате - по убыванию"""
    return sorted(data, key=lambda x: x.get('date'), reverse=True)


def data_clean(file):
    """Функция удаляет пустые строки из списка данных."""
    data = load_data(file)
    data = [item for item in data if item]
    return data


def date_format(value):
    """Функция форматирует дату.("2019-12-08T22:46:21.935582" в 08.12.2019)"""
    return datetime.strftime(datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f').date(), '%d.%m.%Y')


def card_hidden(value):
    """Функция скрывает для карт наборы цифр"""
    val1 = value.split()[-1]
    val2 = value.split(" ")[0:-1][:]
    val1 = val1[0:4] + ' ' + val1[4:6] + (len(val1[-6:-4]) * '*') + ' ' + (
            len(val1[-10:-6]) * '*') + ' ' + val1[-4:]
    val2 = ','.join(val2).replace(',', ' ')
    value = val2 + " " + val1
    return value


def account_hidden(value):
    """Функция скрывает для счета наборы цифр"""
    val1 = str(value.split(" ")[0])
    val2 = str(value.split(" ")[1])
    value = val1 + " " + val2[0:16] + (4 * '*')
    return value

def main_func():
    """ Основная логика программы, которая выводит на экран список из 5 последних выполненных клиентом операций"""
    data = data_clean("operations.json")
    data = sort_status(data)
    sorted_data = sort_data(data)
    for item in sorted_data[:5]:
        from_to = item.get('from', 'not found')
        if from_to == 'not found':
            from_to = from_to
        elif len(str(from_to.split(" ")[-1])) < 20:
            from_to = card_hidden(from_to)
        else:
            from_to = account_hidden(from_to)
        date = date_format(item.get('date'))
        description = item.get("description", 'not found')
        to = item.get("to", 'not found')
        if to == 'not found':
            to = to
        elif len(str(to.split(" ")[-1])) < 20:
            to = card_hidden(to)
        else:
            to = account_hidden(to)
        amount = item.get('operationAmount', 'not found').get('amount', 'not found')
        currency = item.get('operationAmount').get('currency').get('name', 'not found')
        print(f'{date} {description}\n{from_to} -> {to}\n{amount} {currency} \n')