from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['product_database']
collection = db['products']

# Test Data : http://localhost:5002/products/P010

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = collection.find_one({"id": product_id})
    if product:
        product.pop('_id')  # Remove MongoDB's internal ID
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(port=5002)

