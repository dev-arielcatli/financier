from shared.models.expense import ExpenseModel
from shared.utils.requests import extract_query_parameters

from shared.models.urls import QUERY_PARAM_LAST_EVALUATED_KEY

from shared.utils.responses import make_list_response


def handler(event, context):
    last_evaluated = extract_query_parameters(event).get(QUERY_PARAM_LAST_EVALUATED_KEY, None)
    items = ExpenseModel.query(
        hash_key=ExpenseModel.user_id,
        limit=10,
        scan_index_forward=True,
        last_evaluated_key=last_evaluated,
    )

    return make_list_response(items=[item.attribute_values for item in list(items)], last_evaluated_key=items.last_evaluated_key)
    
