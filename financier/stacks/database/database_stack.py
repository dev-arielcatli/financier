import aws_cdk as cdk
from aws_cdk import aws_dynamodb as _ddb

from constructs import Construct


from financier.shared.models.base import ItemModel

from financier.shared.utils.naming import get_app_table_name


class DatabaseStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.table = _ddb.TableV2(
            self,
            get_app_table_name(),
            partition_key=_ddb.Attribute(
                name=ItemModel.userId.attr_name, type=_ddb.AttributeType.STRING
            ),
            table_name=get_app_table_name(),
        )
