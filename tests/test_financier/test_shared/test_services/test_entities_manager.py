from unittest import TestCase

import boto3
import moto
from pynamodb.exceptions import DoesNotExist
from shared.config import APP_NAME, STAGE
from shared.models.expense import ExpenseModel
from shared.services.entities_manager import load_item


@moto.mock_aws
class TestEntitiesManager(TestCase):
    def setUp(self) -> None:
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.create_table(
            TableName=f"{APP_NAME}-{STAGE}-table-main",
            KeySchema=[
                {"AttributeName": "item_id", "KeyType": "RANGE"},
                {"AttributeName": "user_id", "KeyType": "HASH"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "item_id", "AttributeType": "S"},
                {"AttributeName": "user_id", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )

    def test_load_item(self):
        test_expense = ExpenseModel(
            item_id="test_id",
            user_id="system",
            quantity=100,
            name="hotdog",
            description="test_description",
        )
        test_expense.save()
        expected_expense = load_item(ExpenseModel, "test_id")
        self.assertEqual(test_expense.item_id, expected_expense.item_id)

    def test_load_item_not_found(self):
        with self.assertRaises(DoesNotExist):
            load_item(ExpenseModel, "test_id")
