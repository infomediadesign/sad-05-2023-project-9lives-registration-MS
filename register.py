from pymongo import MongoClient


client = MongoClient("mongodb+srv://rajat011:HxXq4k1ODpXQGjw6@dev.ylhokif.mongodb.net/?retryWrites=true&w=majority")
#client = MongoClient('localhost', 27017)
db = client["usersdb"]
collection = db["login-details"]