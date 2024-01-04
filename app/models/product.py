from bson.objectid import ObjectId
from . import mongo

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    @staticmethod
    def to_dict(product):
        return {
            'id': str(product['_id']),
            'name': product['name'],
            'description': product['description'],
            'price': product['price'],
            'orders': [str(order) for order in product['orders']]
        }

    @staticmethod
    def from_db(product_id):
        product = mongo.db.products.find_one({'_id': ObjectId(product_id)})
        return Product.to_dict(product) if product else None

    def save_to_db(self):
        product = {'name': self.name, 'description': self.description, 'price': self.price, 'orders': []}
        result = mongo.db.products.insert_one(product)
        return str(result.inserted_id)
