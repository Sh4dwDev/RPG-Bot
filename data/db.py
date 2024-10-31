from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb+srv://ShadowDev:ArneG200604@gandalf.qwrbc.mongodb.net/?retryWrites=true&w=majority&appName=Gandalf")
    return client["bot_database"]

