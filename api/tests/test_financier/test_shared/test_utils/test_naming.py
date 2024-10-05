from unittest import TestCase

from shared.config import APP_NAME, STAGE
from shared.models.actions import Action
from shared.models.features import Feature
from shared.utils import naming


class TestNaming(TestCase):

    def test_compose(self):
        self.assertEqual(naming.compose(["test", "name"]), "test-name")

    def test_get_function_name(self):
        self.assertEqual(
            naming.get_function_name("test", Feature.EXPENSE, Action.GET),
            f"{APP_NAME}-{STAGE}-function-expense-test-get",
        )

    def test_get_function_handler_path(self):
        self.assertEqual(
            naming.get_function_handler_path(Feature.EXPENSE, Action.GET),
            "stacks.functions.handlers.expense.get.handler",
        )

    def test_get_layer_name(self):
        self.assertEqual(
            naming.get_layer_name("test"), f"{APP_NAME}-{STAGE}-layer-test"
        )

    def test_function_role_name(self):
        self.assertEqual(
            naming.get_function_role_name("test"),
            f"{APP_NAME}-{STAGE}-function-role-test",
        )

    def test_default_function_role_name(self):
        self.assertEqual(
            naming.get_default_function_role_name(),
            f"{APP_NAME}-{STAGE}-function-role-default",
        )

    def test_get_table_name(self):
        self.assertEqual(
            naming.get_table_name("test"), f"{APP_NAME}-{STAGE}-table-test"
        )

    def test_get_app_table_name(self):
        self.assertEqual(naming.get_app_table_name(), f"{APP_NAME}-{STAGE}-table-main")

    def test_get_app_table_role_name(self):
        self.assertEqual(
            naming.get_app_table_role_name("test"),
            f"{APP_NAME}-{STAGE}-table-test-role",
        )

    def test_get_api_name(self):
        self.assertEqual(naming.get_api_name("test"), f"{APP_NAME}-{STAGE}-api-test")

    def test_get_api_stack_name(self):
        self.assertEqual(
            naming.get_api_stack_name(), f"{APP_NAME}-{STAGE}-stack-apigateway"
        )

    def test_get_deployment_name(self):
        self.assertEqual(naming.get_deployment_name(), f"{APP_NAME}-deployment-{STAGE}")

    def test_get_stage_name(self):
        self.assertEqual(naming.get_stage_name(), f"{APP_NAME}-stage-{STAGE}")

    def test_get_stack_name(self):
        self.assertEqual(
            naming.get_stack_name("test"), f"{APP_NAME}-{STAGE}-stack-test"
        )

    def test_get_database_stack_name(self):
        self.assertEqual(
            naming.get_database_stack_name(), f"{APP_NAME}-{STAGE}-stack-database"
        )

    def test_get_functions_stack_name(self):
        self.assertEqual(
            naming.get_functions_stack_name(), f"{APP_NAME}-{STAGE}-stack-functions"
        )

    def test_get_api_gateway_stack_name(self):
        self.assertEqual(
            naming.get_api_gateway_stack_name(), f"{APP_NAME}-{STAGE}-stack-apigateway"
        )
