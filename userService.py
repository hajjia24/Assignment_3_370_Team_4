from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['user_database']
collection = db['users']


# Test Data : http://127.0.0.1:5000/users/1


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = collection.find_one({"id": user_id})
    if user:
        user.pop('_id')  # Remove MongoDB's internal ID
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)