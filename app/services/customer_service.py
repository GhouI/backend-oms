from .models import Customer

def create_customer(name, email):
    customer = Customer(name=name, email=email)
    db.session.add(customer)
    db.session.commit()
    return customer

def get_customer_by_id(customer_id):
    return Customer.query.get(customer_id)

def get_all_customers():
    return Customer.query.all()

def update_customer(customer_id, name, email):
    customer = get_customer_by_id(customer_id)
    customer.name = name
    customer.email = email
    db.session.commit()
    return customer

def delete_customer(customer_id):
    customer = get_customer_by_id(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return customer
    
