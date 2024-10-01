from typing import Type
from shared.models.base import ItemModel

from shared.config import DEFAULT_SYSTEM_ID

def load_item(model_type: Type[ItemModel], item_id: any, hash_key: str = DEFAULT_SYSTEM_ID):
    return model_type.get(hash_key=hash_key, range_key=item_id)