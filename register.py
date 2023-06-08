from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, jsonify
from flasgger import Swagger, swag_from

client = MongoClient("mongodb+srv://rajat011:HxXq4k1ODpXQGjw6@dev.ylhokif.mongodb.net/?retryWrites=true&w=majority")
#client = MongoClient('localhost', 27017)
db = client["usersdb"]
collection = db["login-details"]

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
def home():
    return "Welcome to the registration page!"


@app.route("/register", methods=["GET", "POST"])
@swag_from('swagger/register.yml')
def register():
    if request.method == "POST":
        
        user_email = request.form["user-email"]
        password = request.form["password"]

        

        existing_user = collection.find_one({"user-email": user_email})
        if existing_user:
            return "Email is already registered!"
        
        
        new_user = {
            "user-email": user_email,
            "password": password
        }

        collection.insert_one(new_user)

        
        return jsonify({'message': 'Registration successful'}), 201
    else:
        
        return render_template("register.html")

@app.route("/success")
def success():
    return "Registration successful!"

if __name__ == "__main__":
    app.run(debug=True)