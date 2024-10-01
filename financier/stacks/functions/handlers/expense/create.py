from shared.utils.requests import extract_body
from shared.utils.responses import make_response, make_error_response

from shared.models.expense import ExpenseModel, ExpensePydanticModel
from http import HTTPStatus
from shared.utils.modeling import generate_uuid
from shared.models.errors import ErrorCodes

from pydantic import ValidationError

def handler(event, context):
    body = extract_body(event)
    print(body)
    try:
        expense = ExpensePydanticModel(**body)
    except ValidationError as error:
        return make_error_response(error_code=ErrorCodes.INVALID_EXPENSE,
                                   status=HTTPStatus.BAD_REQUEST,
                                   body=error.errors())
    
    new_expense = ExpenseModel(**expense.model_dump())
    new_expense.item_id = generate_uuid()
    new_expense.save()

    return make_response(body=new_expense.attribute_values, status=HTTPStatus.CREATED)