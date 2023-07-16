"""Income Class and Income Schema"""
from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType


class Income(Transaction):
    """Income Class"""
    def __init__(self, description, amount):
        super().__init__(description, amount, TransactionType.INCOME)

    def __repr__(self):
        return '<Income(name={self.description!r})>'.format(self=self)


class IncomeSchema(TransactionSchema):
    """Income Schema"""
    @post_load
    def make_income(self, data, **kwargs):
        """Return income data"""
        return Income(**data)
