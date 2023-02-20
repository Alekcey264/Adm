from models import *
from helper import *

def test_createBD_true():
    assert createDB() == True

def test_fillClients_true():
    assert client.name == True
    assert client.city == True
    assert client.address == True

def test_fillOrders_true():
    assert order.client == True
    assert order.date == True
    assert order.amount ==True
    assert order.description == True

def test_countClients():
    fillDB()
    assert show_clients()

def test_countOrders():
    fillDB()
    assert show_orders()

# pytestСЃ --junitxml=result.xml 