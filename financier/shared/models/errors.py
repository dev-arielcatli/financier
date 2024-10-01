from enum import Enum


class ErrorCodes(Enum):
    MISSING_EXPENSE = "missing_expense"
    INVALID_EXPENSE = "invalid_expense"
    UNHANDLED_ERROR = "unhandled_error"
