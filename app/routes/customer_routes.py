from flask import Blueprint, jsonify, request
from .services import customer_service
from bson import json_util

bp = Blueprint('customers', __name__, url_prefix='/customers')

@bp.route('/', methods=['GET'])
def get_customers():
    customers = customer_service.get_all_customers()
    return jsonify(json_util.dumps([customer.to_dict() for customer in customers]))

@bp.route('/', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = customer_service.create_customer(data['name'], data['email'])
    return jsonify(json_util.dumps(customer.to_dict())), 201
