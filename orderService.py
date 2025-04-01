from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['order_database']
collection = db['orders']

@app.route('/orders', methods=['GET'])
def get_orders_by_user():
    user_id = request.args.get('user_id')
    user_orders = list(collection.find({"user_id": user_id}))
    for order in user_orders:
        order.pop('_id')  # Remove MongoDB's internal ID
    return jsonify(user_orders)

if __name__ == '__main__':
    app.run(port=5001)
