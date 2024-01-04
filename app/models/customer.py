from bson.objectid import ObjectId
from . import mongo

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def to_dict(customer):
        return {
            'id': str(customer['_id']),
            'name': customer['name'],
            'email': customer['email'],
            'orders': [str(order) for order in customer['orders']]
        }

    @staticmethod
    def from_db(customer_id):
        customer = mongo.db.customers.find_one({'_id': ObjectId(customer_id)})
        return Customer.to_dict(customer) if customer else None

    def save_to_db(self):
        customer = {'name': self.name, 'email': self.email, 'orders': []}
        result = mongo.db.customers.insert_one(customer)
        return str(result.inserted_id)
