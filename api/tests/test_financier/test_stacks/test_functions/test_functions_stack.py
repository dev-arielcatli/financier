from unittest import TestCase

import aws_cdk as cdk
from stacks.database.database_stack import DatabaseStack
from stacks.functions.functions_stack import FunctionsStack


class TestFunctionsStack(TestCase):
    def setUp(self) -> None:
        self.app = cdk.App()
        self.mock_database_stack = DatabaseStack(self.app, "TestDatabaseStack")
        self.functions_stack = FunctionsStack(
            self.app, "TestFunctionsStack", database_stack=self.mock_database_stack
        )
        self.template = cdk.assertions.Template.from_stack(self.functions_stack)

    def test_creation_of_layer(self):
        self.template.resource_count_is("AWS::Lambda::LayerVersion", 1)

    def test_creation_of_expense_functions(self):
        self.template.resource_count_is("AWS::Lambda::Function", 6)
