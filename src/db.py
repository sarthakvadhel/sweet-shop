from pymongo import MongoClient

def get_mongo_collection(db_name="sweetshop", collection_name="sweets"):
    client = MongoClient("mongodb://localhost:27017")  # change this if using Atlas
    db = client[db_name]
    return db[collection_name]
