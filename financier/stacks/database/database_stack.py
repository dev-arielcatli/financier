import aws_cdk as cdk
from aws_cdk import aws_dynamodb as _ddb
from aws_cdk import aws_iam as _iam
from constructs import Construct
from shared.models.base import ItemModel
from shared.utils.naming import get_app_table_name, get_app_table_role_name


class DatabaseStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self.table = _ddb.TableV2(
            self,
            get_app_table_name(),
            partition_key=_ddb.Attribute(
                name=ItemModel.user_id.attr_name, type=_ddb.AttributeType.STRING
            ),
            sort_key=_ddb.Attribute(
                name=ItemModel.item_id.attr_name, type=_ddb.AttributeType.STRING
            ),
            table_name=get_app_table_name(),
        )

        self.create_db_policies()

    def create_db_policies(self):
        self.reader_writer_policy = _iam.PolicyStatement(
            actions=[
                "dynamodb:BatchGetItem",
                "dynamodb:DescribeGlobalTable",
                "dynamodb:DescribeGlobalTableSettings",
                "dynamodb:DescribeLimits",
                "dynamodb:DescribeReservedCapacity",
                "dynamodb:DescribeReservedCapacityOfferings",
                "dynamodb:DescribeStream",
                "dynamodb:DescribeTable",
                "dynamodb:DescribeTimeToLive",
                "dynamodb:GetItem",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:Query",
                "dynamodb:DescribeStream",
                "dynamodb:PutItem",
                "dynamodn:DeleteItem",
                "dynamodb:BatchWriteItem",
                "dynamodb:UpdateItem",
                "dynamodb:ListStreams",
            ],
            resources=[self.table.table_arn],
        )
