from pynamodb.attributes import ListAttribute, NumberAttribute, UnicodeAttribute

from shared.config import AWS_DEFAULT_REGION, DEFAULT_UNIT
from shared.models.base import ItemModel, ItemTypes
from shared.utils.naming import get_app_table_name


class ExpenseModel(ItemModel):
    class Meta:
        table_name = get_app_table_name()
        region = AWS_DEFAULT_REGION

    type = UnicodeAttribute(null=False, default=ItemTypes.EXPENSE.value)

    name = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=True)
    place = UnicodeAttribute(null=True)

    categories = ListAttribute(of=UnicodeAttribute, null=False, default=())

    quantity = NumberAttribute(null=False, default=1)
    unit = UnicodeAttribute(null=False, default=DEFAULT_UNIT)
    unit_price = NumberAttribute(null=False, default=1)
