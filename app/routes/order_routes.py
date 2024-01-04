from flask import Blueprint, jsonify, request
from .services import order_service
from bson import json_util

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('/', methods=['GET'])
def get_orders():
    orders = order_service.get_all_orders()
    return jsonify(json_util.dumps([order.to_dict() for order in orders]))

@bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    order = order_service.create_order(data['product_name'], data['customer_name'], data['quantity'])
    return jsonify(json_util.dumps(order.to_dict())), 201
