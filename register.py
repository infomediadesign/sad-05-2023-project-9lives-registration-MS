from pymongo import MongoClient
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

client = MongoClient(
    "mongodb+srv://rajat011:HxXq4k1ODpXQGjw6@dev.ylhokif.mongodb.net/?retryWrites=true&w=majority")
# client = MongoClient('localhost', 27017)
db = client["usersdb"]
collection = db["login-details"]

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/")
def home():
    return jsonify({'message': "Welcome to the registration page!"})


@app.route("/register", methods=["POST"])
@swag_from('swagger/register.yml')
def register():
    if request.method == "POST":

        user_email = request.form["email"]
        password = request.form["password"]

        existing_user = collection.find_one({"email": user_email})
        if existing_user:
            return "Email is already registered!"

        new_user = {
            "email": user_email,
            "password": password
        }

        collection.insert_one(new_user)

        return jsonify({'message': 'Registration successful'}), 201
    else:

        return jsonify({'message': 'Registration unsuccessful'}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5001)
