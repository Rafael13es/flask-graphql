""""Expense Class and Expense Schema"""
from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType


class Expense(Transaction):
    """Expense Class"""
    def __init__(self, description, amount):
        super().__init__(description, -abs(amount), TransactionType.EXPENSE)

    def __repr__(self):
        return '<Expense(name={self.description!r})>'.format(self=self)


class ExpenseSchema(TransactionSchema):
    """Expense Schema"""
    @post_load
    def make_expense(self, data, **kwargs):
        """
        Get the expense data in json and serialize
        as Expense object
        :param data: json expense data
        :param kwargs:
        :return: Expense
        """
        return Expense(**data)
