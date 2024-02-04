from ..functions import *
import pytest


def test_sort_data():
    pass


def test_sort_status(value):
    assert sort_status(value) == 'EXECUTED'


def test_data_clean(data):
    assert data_clean(data) == data


def test_load_data(value):
    assert load_data(value) == value


def test_date_format():
    assert date_format("2019-12-08T22:46:21.935582") == "08.12.2019"


def test_card_hidden(value):
    assert card_hidden(len(value)) == 20


def test_account_hidden(value):
    assert account_hidden(len(value)) == 16
