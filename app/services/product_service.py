from .models import product 

def create_product(name, description, price):
    product = product(name=name, description=description, price=price)
    db.session.add(product)
    db.session.commit()
    return product

def get_product_by_id(product_id):
    return product.query.get(product_id)

def get_all_products():
    return product.query.all()

def update_product(product_id, name, description, price):
    product = get_product_by_id(product_id)
    product.name = name
    product.description = description
    product.price = price
    db.session.commit()
    return product

def delete_product(product_id):
    product = get_product_by_id(product_id)
    db.session.delete(product)
    db.session.commit()
    return product

