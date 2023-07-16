"""Transaction Type"""
from enum import Enum


class TransactionType(Enum):
    """Transaction Type Enum"""
    INCOME = "Income"
    EXPENSE = "Expense"
