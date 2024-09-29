from financier.shared.utils.naming import get_app_table_name
from financier.shared.models.base import ItemModel, ItemTypes
from financier.shared.config import AWS_DEFAULT_REGION, DEFAULT_UNIT

from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute


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
    unitPrice = NumberAttribute(null=False, default=1)
