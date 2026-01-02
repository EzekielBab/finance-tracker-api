from flask import Blueprint, request, jsonify
from sqlalchemy import extract
from .models import Transaction
from . import db

main = Blueprint("main", __name__)

@main.route("/transactions", methods=["POST"])
def add_transaction():
    data = request.json
    transaction = Transaction(
        amount=data["amount"],
        category=data["category"],
        type=data["type"]
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added"}), 201

@main.route("/transactions", methods=["GET"])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([t.to_dict() for t in transactions])

@main.route("/summary/<int:month>", methods=["GET"])
def monthly_summary(month):
    expenses = Transaction.query.filter(
        Transaction.type == "expense",
        extract("month", Transaction.date) == month
    ).all()

    total = sum(t.amount for t in expenses)

    return jsonify({
        "month": month,
        "total_expenses": total
    })