from ..functions import data_clean, sort_data, sort_status, card_hidden, \
    account_hidden, date_format, load_data
from ..main import main
import json


def test_sort_data():
    with (open("operations.json", encoding="utf-8") as f):
        data = json.load(f)
        assert sort_data(data) == data


def test_sort_status():
    with open("template_dict_sort.json", encoding="utf-8") as f:
        data = json.load(f)
        assert sort_status(data) == data


def test_data_clean():
    assert data_clean("template_dict_sort.json") != 'Error'


def test_load_data():
    assert load_data("operations.json") == load_data("operations.json")


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
     assert main() == main()
