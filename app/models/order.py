from bson.objectid import ObjectId
from . import mongo

class Order:
    def __init__(self, product_name, customer_name, quantity):
        self.product_name = product_name
        self.customer_name = customer_name
        self.quantity = quantity

    @staticmethod
    def to_dict(order):
        return {
            'id': str(order['_id']),
            'product_name': order['product_name'],
            'customer_name': order['customer_name'],
            'quantity': order['quantity']
        }

    @staticmethod
    def from_db(order_id):
        order = mongo.db.orders.find_one({'_id': ObjectId(order_id)})
        return Order.to_dict(order) if order else None

    def save_to_db(self):
        order = {'product_name': self.product_name, 'customer_name': self.customer_name, 'quantity': self.quantity}
        result = mongo.db.orders.insert_one(order)
        return str(result.inserted_id)
