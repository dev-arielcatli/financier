from unittest import TestCase

import aws_cdk as cdk
from stacks.database.database_stack import DatabaseStack

from shared.config import STAGE, APP_NAME

class TestDatabaseStack(TestCase):
    def setUp(self):
        self.app = cdk.App()
        self.database_stack = DatabaseStack(self.app, "TestDatabaseStack")
        self.template = cdk.assertions.Template.from_stack(self.database_stack)

    def test_creation_of_global_table(self):
        self.assertTrue(self.database_stack)
        self.template.resource_count_is("AWS::DynamoDB::GlobalTable", 1)
        self.template.has_resource_properties(
            "AWS::DynamoDB::GlobalTable",
            {
                "TableName": f"{APP_NAME}-{STAGE}-table-main",
                "KeySchema": [
                    {"AttributeName": "user_id", "KeyType": "HASH"},
                    {"AttributeName": "item_id", "KeyType": "RANGE"},
                ],
            },
        )
        important_policies = [
            "dynamodb:GetItem",
            "dynamodb:PutItem",
            "dynamodb:UpdateItem",
            "dynamodb:DeleteItem",
        ]
        for policy in important_policies:
            self.assertIn(policy, self.database_stack.reader_writer_policy.actions)
