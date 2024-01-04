from flask import Blueprint, jsonify, request
from .services import product_service
from bson import json_util

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
    products = product_service.get_all_products()
    return jsonify(json_util.dumps([product.to_dict() for product in products]))

@bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = product_service.create_product(data['name'], data['description'], data['price'])
    return jsonify(json_util.dumps(product.to_dict())), 201
