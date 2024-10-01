from enum import Enum

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from shared.config import DEFAULT_SYSTEM_ID
from shared.utils.naming import get_app_table_name
from typing import Optional
from pydantic import BaseModel, field_serializer

from datetime import datetime

class ItemTypes(Enum):
    EXPENSE = "expense"
    INCOME = "income"
    DEFAULT = "default"


class ItemModel(Model):
    class Meta:
        table_name = get_app_table_name()

    user_id = UnicodeAttribute(hash_key=True, default=DEFAULT_SYSTEM_ID)
    created_at = UTCDateTimeAttribute(null=False, range_key=True)
    type = UnicodeAttribute(null=False, default=ItemTypes.DEFAULT.value)

    updated_at = UTCDateTimeAttribute(null=True)
    item_id = UnicodeAttribute(null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_date_fields()

    def update_date_fields(self):
        now = datetime.now()
        self.updated_at = now
        if not self.created_at:
            self.created_at = now

class ItemPydanticModel(BaseModel):
    user_id: str
    created_at: Optional[datetime] = None
    type: ItemTypes = ItemTypes.DEFAULT.value
    updated_at: Optional[datetime] = None
    item_id: Optional[str] = None

    @field_serializer('type')
    def serialize_type(value: ItemTypes) -> str:
        return value.value