import json


def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Get expense"}),
    }
from shared.utils.requests import extract_body
from shared.utils.responses import make_response, make_error_response

from shared.models.expense import ExpenseModel, ExpensePydanticModel
from http import HTTPStatus
from shared.models.errors import ErrorCodes

from pynamodb.exceptions import PutError

from pydantic import ValidationError

def handler(event, context):
    body = extract_body(event)
    try:
        expense = ExpensePydanticModel(**body)
    except ValidationError as error:
        return make_error_response(error_code=ErrorCodes.INVALID_EXPENSE,
                                   status=HTTPStatus.BAD_REQUEST,
                                   body=error.errors())
    
    expense_to_update = ExpenseModel(**expense.model_dump())
    
    try:
        expense_to_update.save(ExpenseModel.item_id.exists())
    except PutError as error:
        if error.cause_response_code == "ConditionalCheckFailedException":
            return make_error_response(error_code=ErrorCodes.MISSING_EXPENSE, status=HTTPStatus.NOT_FOUND)
        else:
            return make_error_response(error_code=ErrorCodes.FAILED_UPDATE, status=HTTPStatus.INTERNAL_SERVER_ERROR)

    return make_response(body=expense_to_update.attribute_values, status=HTTPStatus.OK)

