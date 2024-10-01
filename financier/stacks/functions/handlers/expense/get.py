from http import HTTPStatus

from shared.config import DEFAULT_SYSTEM_ID
from shared.models.errors import ErrorCodes
from shared.models.expense import ExpenseModel
from shared.models.urls import EXPENSE_ID
from shared.utils.requests import extract_path_parameters
from shared.utils.responses import make_error_response, make_response

from shared.services.entities_manager import load as load_expense


def handler(event, context):
    expense_id = extract_path_parameters(event)[EXPENSE_ID]
    items_list = load_expense(model_type=ExpenseModel, item_id=DEFAULT_SYSTEM_ID, range_key_condition=ExpenseModel.item_id == expense_id)
    if not items_list:
        return make_error_response(ErrorCodes.MISSING_EXPENSE, HTTPStatus.NOT_FOUND)

    return make_response(items_list[0].attribute_values)