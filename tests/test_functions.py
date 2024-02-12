from functions import sort_data, sort_status, card_hidden, \
    account_hidden, date_format, load_data
from main import main
import json


def test_sort_data():
    with (open("../operations.json", encoding="utf-8") as f):
        data = json.load(f)
        assert sort_data(data)[0]['date'] == '2019-12-08T22:46:21.935582'


def test_sort_status():
    with open("template_dict_sort.json", encoding="utf-8") as f:
        data = json.load(f)
        assert sort_status(data)[0]['state'] == 'EXECUTED'



def test_load_data():
    with open('temp_operation.json', encoding="utf-8") as file:
        file = json.load(file)
        assert load_data('../operations.json') == file


def test_date_format():
    assert date_format("2019-12-08T22:46:21.935582") == "08.12.2019"


def test_card_hidden():
    with open("template_dict.json", encoding="utf-8") as f:
        data = json.load(f)
        data = data.get('from', 'not found')
        assert card_hidden(data) == 'Visa Classic 2842 87** **** 9012'


def test_account_hidden():
    with open("template_dict.json", encoding="utf-8") as f:
        data = json.load(f)
        data = data.get('to', 'not found')
        assert account_hidden(data) == 'Счет 3515858638461075****'


def test_main():
    assert len(main()) == 5
