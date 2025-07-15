from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item = {
        "name": request.form['itemName'],
        "description": request.form['itemDescription']
    }
    collection.insert_one(item)
    return "Item submitted successfully!"
