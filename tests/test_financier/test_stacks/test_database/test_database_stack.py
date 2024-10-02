from unittest import TestCase
from stacks.database.database_stack import DatabaseStack

import aws_cdk as cdk

class TestDatabaseStack(TestCase):
    def setUp(self):
        self.app = cdk.App()
        self.database_stack = DatabaseStack(self.app, "TestDatabaseStack")
        self.template = cdk.assertions.Template.from_stack(self.database_stack)

    def test_creation_of_global_table(self):
        self.assertTrue(self.database_stack)
        self.template.resource_count_is("AWS::DynamoDB::GlobalTable", 1)
        self.template.has_resource_properties("AWS::DynamoDB::GlobalTable", {
            "TableName": "financier-dev-table-main",
            "KeySchema": [
                {
                    "AttributeName": "user_id",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "item_id",
                    "KeyType": "RANGE"
                }
            ],
        })