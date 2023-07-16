"""App"""
from flask import Flask, jsonify, request
from .model.expense import Expense, ExpenseSchema
from .model.income import Income, IncomeSchema
from .model.transaction_type import TransactionType

app = Flask(__name__)


transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]


@app.route('/incomes')
def get_incomes():
    """get incomes"""
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    """add income"""
    incomes = IncomeSchema().load(request.get_json())
    transactions.append(incomes)
    return '', 201


@app.route('/expenses')
def get_expenses():
    """get expense"""
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses)


@app.route('/expenses', methods=['POST'])
def add_expense():
    """add expense"""
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return '', 201


if __name__ == "__main__":
    app.run()
