from peewee import *

database_path = "db/datebase.db"
db = SqliteDatabase(database_path)

class BaseModel(Model):
    id = PrimaryKeyField(unique = True)

    class Meta:
        database = db
        order_by = "id"

class client(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()

    class Meta:
        db_table = 'CLIENTS'

class order(BaseModel):
    client = ForeignKeyField(client)
    date = DateField()
    amount = IntegerField()
    description = TextField()

    class Meta:
        db_table = 'ORDERS'