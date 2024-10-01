from typing import Type
from shared.models.base import ItemModel

def load(model_type: Type[ItemModel], item_id: any, filter_condition: any = None):
    items = model_type.query(
        hash_key=item_id,
        filter_condition=filter_condition
    ) 
    return list(items)