from models import *
from lists import *
import random
import os
from os import remove, path

def working_with_parameter(parameter):
    if parameter.lower() == "init":
        if os.path.isfile(database_path):
            os.remove(database_path)
        with db:
            db.create_tables([client, order])
            #asdasdasd
    elif parameter.lower() == "fill":
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
            client.insert_many(list_for_insert_into_clients).execute()
            order.insert_many(list_for_insert_into_orders).execute()
    elif parameter.lower() == "show clients":
        if os.path.isfile(database_path):
            all_info_from_table_clients = client.select()   
            for paragraph in all_info_from_table_clients:
                print(paragraph.id, paragraph.name, paragraph.city, paragraph.address)
    elif parameter.lower() == "show orders":
        if os.path.isfile(database_path):
            all_info_from_table_orders = order.select()
            for paragraph in all_info_from_table_orders:
                print(paragraph.id, paragraph.client_id, paragraph.date, paragraph.amount, paragraph.description)
    else:
        print("Parameter error")