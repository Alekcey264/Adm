from models import *
from lists import *
import random, os
from os import remove, path

def createDB():
    if os.path.isfile(database_path):
        os.remove(database_path)
    with db:
        db.create_tables([client, order])
    return True

def fillDB():
    if os.path.isfile(database_path):
        list_for_insert_into_clients = []
        list_for_insert_into_orders = []
        n = random.randint(1, 100)
        for _ in range(n):
            j = random.randint(0, len(NAME) - 1)
            list_for_insert_into_clients.append({"name":random.choice(NAME), "city":CITY[j], "address":ADDRESS[j]})
        for _ in range(random.randint(n, 150)):
            list_for_insert_into_orders.append({"client_id":random.randint(1, n), "date":random.choice(DATE), 
                                            "amount":random.randint(1, 200), "description":random.choice(DESCRIPTION)})
        with db:
            client.insert_many(list_for_insert_into_clients).execute()
            order.insert_many(list_for_insert_into_orders).execute()
        return True
    else:
        print("The database does not exist, to start working with it, enter the command 'init'")

def show_clients():
    if os.path.isfile(database_path):
        all_info_from_table_clients = client.select()   
        for paragraph in all_info_from_table_clients:
            print(paragraph.id, paragraph.name, paragraph.city, paragraph.address)
        return True
    else:
        print("The database does not exist, to start working with it, enter the command 'init'")

def show_orders():
    if os.path.isfile(database_path):
        all_info_from_table_orders = order.select()
        for paragraph in all_info_from_table_orders:
            print(paragraph.id, paragraph.client_id, paragraph.date, paragraph.amount, paragraph.description)
        return True   
    else:
        print("The database does not exist, to start working with it, enter the command 'init'")

def main():
    parameter = input()
    if parameter == "init":
        createDB()
    elif parameter == "fill":
        fillDB()
    elif parameter.lower() == "show clients":
        show_clients()
    elif parameter.lower() == "show orders":
        show_orders()
    else:
        print("You entered an invalid parameter value.\nProgram execution stopped.")