import json
from shared.services.entities_manager import load_item as load_expense
from shared.utils.requests import extract_path_parameters

from shared.models.expense import ExpenseModel
from pynamodb.exceptions import DoesNotExist

from shared.utils.responses import make_error_response, make_response

from shared.models.errors import ErrorCodes
from http import HTTPStatus

from shared.models.urls import EXPENSE_ID

def handler(event, context):
    expense_id = extract_path_parameters(event)[EXPENSE_ID]

    try:
        expense = load_expense(model_type=ExpenseModel, item_id=expense_id)
    except DoesNotExist:
        return make_error_response(status=HTTPStatus.NOT_FOUND, error_code=ErrorCodes.MISSING_EXPENSE)
    
    expense.delete()
    return make_response(None, status=HTTPStatus.NO_CONTENT)
