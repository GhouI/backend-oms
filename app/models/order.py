from . import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(128))
    customer_name = db.Column(db.String(128))
    quantity = db.Column(db.Integer)
