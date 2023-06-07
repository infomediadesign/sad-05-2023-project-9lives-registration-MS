from pymongo import MongoClient
from flask import Flask, render_template, request, redirect

client = MongoClient("mongodb+srv://rajat011:HxXq4k1ODpXQGjw6@dev.ylhokif.mongodb.net/?retryWrites=true&w=majority")
#client = MongoClient('localhost', 27017)
db = client["usersdb"]
collection = db["login-details"]

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the registration page!"

if __name__ == "__main__":
    app.run(debug=True)