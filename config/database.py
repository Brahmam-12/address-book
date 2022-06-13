import collections
from pymongo import MongoClient

client = MongoClient("mongodb+srv://brahmam-05:Brahmam123@cluster0.kvjmo.mongodb.net/?retryWrites=true&w=majority")
db = client.address_application


collection_name = db["address_app"]