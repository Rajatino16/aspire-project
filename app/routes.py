from flask import Blueprint, request, jsonify
from .models import Loan

main = Blueprint('main', __name__)

@main.route('/loan', methods=['POST'])
def create_loan():
    data = request.get_json()
    amount = data['amount']
    term = data['term']
    # For demonstration purposes, assuming user_id is passed in request
    user_id = data['user_id']
    loan = Loan.create_loan(amount, term, user_id)
    return jsonify({"message": "Loan created successfully!", "loan": loan}), 201

@main.route('/loans', methods=['GET'])
def get_loans():
    # For demonstration purposes, assuming user_id is passed in query string
    user_id = request.args.get('user_id')
    print("loan being fetched for ", user_id)
    loans = Loan.get_loans(user_id)
    return jsonify({"loans": loans}), 200

@main.route('/loan/approve/<int:loan_id>', methods=['POST'])
def approve_loan(loan_id):
    success, message = Loan.approve_loan(loan_id)
    if success:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"message": message}), 400

@main.route('/repayment/<int:loan_id>/<int:repayment_id>', methods=['POST'])
def add_repayment(loan_id, repayment_id):
    data = request.get_json()
    amount = data['amount']
    user_id = data['user_id']
    success, message = Loan.add_repayment(loan_id, repayment_id, amount, int(user_id))
    if success:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"message": message}), 400
