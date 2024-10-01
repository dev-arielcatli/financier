from shared.models.expense import ExpenseModel
from shared.utils.requests import extract_multi_value_query_parameters

from shared.models.urls import QUERY_PARAM_LAST_EVALUATED_KEY

from shared.utils.responses import make_list_response

from shared.config import DEFAULT_SYSTEM_ID


def handler(event, context):
    keys = extract_multi_value_query_parameters(event).get(QUERY_PARAM_LAST_EVALUATED_KEY, None)
    last_evaluated_key = None
    if keys:
        last_evaluated_key = compose_last_evaluated_key(keys)
    items = ExpenseModel.query(hash_key=DEFAULT_SYSTEM_ID,
                                last_evaluated_key=last_evaluated_key)
    iterated_items = []
    limit = 10
    for index, item in enumerate(items):
        if index >= limit:
            break
        iterated_items.append(item.attribute_values)
            
    return make_list_response(items=iterated_items, last_evaluated_key=items.last_evaluated_key)

def compose_last_evaluated_key(keys: dict) -> dict:
    user_id, created_at = keys
    last_evaluated_key = generate_key(user_id, created_at)
    return last_evaluated_key

def generate_key(user_id: str, created_at: str) -> dict:
    return {
            ExpenseModel.user_id.attr_name: {
                "S": user_id
            },
            ExpenseModel.created_at.attr_name: {
                "S": created_at
            }
        }