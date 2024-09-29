from pynamodb.models import Model

from financier.shared.utils.naming import get_app_table_name

from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)

from financier.shared.config import DEFAULT_SYSTEM_ID

from enum import Enum


class ItemTypes(Enum):
    EXPENSE = 'expense'
    INCOME = 'income'
    DEFAULT = 'default'


class ItemModel(Model):
    class Meta:
        table_name = get_app_table_name()

    userId = UnicodeAttribute(hash_key=True, default=DEFAULT_SYSTEM_ID)
    createdAt = UTCDateTimeAttribute(null=False, range_key=True)
    updatedAt = UTCDateTimeAttribute(null=True)

    type = UnicodeAttribute(null=False, default=ItemTypes.DEFAULT.value)
