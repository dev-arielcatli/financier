from enum import Enum

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

from financier.shared.config import DEFAULT_SYSTEM_ID
from financier.shared.utils.naming import get_app_table_name


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
