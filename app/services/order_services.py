from .models import Order

def create_order(product_name, customer_name, quantity):
    order = Order(product_name=product_name, customer_name=customer_name, quantity=quantity)
    db.session.add(order)
    db.session.commit()
    return order

def get_order_by_id(order_id):
    return Order.query.get(order_id)

def get_all_orders():
    return Order.query.all()
