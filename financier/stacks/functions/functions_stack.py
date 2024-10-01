import os

import aws_cdk as cdk
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from constructs import Construct
from shared.config import APP_NAME, FUNCTION_CODE_ROOT_PATH, STAGE
from shared.models.actions import Action
from shared.models.features import Feature
from shared.utils.naming import (
    get_function_handler_path,
    get_function_name,
    get_function_role_name,
    get_layer_name,
)
from stacks.database.database_stack import DatabaseStack


class FunctionsStack(cdk.Stack):
    def __init__(
        self, scope: Construct, id: str, database_stack: DatabaseStack, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.GLOBAL_ENVIRONMENT = {"STAGE": STAGE, "APP_NAME": APP_NAME}
        self.create_layer()
        self.create_expense_functions(database_stack)

    def create_expense_functions(self, database_stack: DatabaseStack):
        # MAIN EXPENSE
        expense_main_function_id = get_function_name(
            name=Feature.EXPENSE.value,
            feature=Feature.EXPENSE,
            action=Action.MAIN,
        )
        self.expense_main_function = _lambda.Function(
            self,
            expense_main_function_id,
            function_name=expense_main_function_id,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset(FUNCTION_CODE_ROOT_PATH),
            handler=get_function_handler_path(
                feature=Feature.EXPENSE,
                action=Action.MAIN,
            ),
        )

        # GET EXPENSE
        expense_get_function_id = get_function_name(
            name=Feature.EXPENSE.value,
            feature=Feature.EXPENSE,
            action=Action.GET,
        )
        self.expense_get_function = _lambda.Function(
            self,
            expense_get_function_id,
            function_name=expense_get_function_id,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset(FUNCTION_CODE_ROOT_PATH),
            handler=get_function_handler_path(
                feature=Feature.EXPENSE,
                action=Action.GET,
            ),
            layers=[self.python_layer],
            role=self.create_function_role(
                f"{Feature.EXPENSE.value}-{Action.GET.value}",
                [database_stack.reader_policy],
            ),
            environment=self.GLOBAL_ENVIRONMENT,
        )

        # CREATE EXPENSE
        expense_create_function_id = get_function_name(
            name=Feature.EXPENSE.value,
            feature=Feature.EXPENSE,
            action=Action.CREATE,
        )
        self.expense_create_function = _lambda.Function(
            self,
            expense_create_function_id,
            function_name=expense_create_function_id,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset(FUNCTION_CODE_ROOT_PATH),
            handler=get_function_handler_path(
                feature=Feature.EXPENSE,
                action=Action.CREATE,
            ),
        )

        # UPDATE EXPENSE
        expense_update_function_id = get_function_name(
            name=Feature.EXPENSE.value,
            feature=Feature.EXPENSE,
            action=Action.UPDATE,
        )
        self.expense_update_function = _lambda.Function(
            self,
            expense_update_function_id,
            function_name=expense_update_function_id,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset(FUNCTION_CODE_ROOT_PATH),
            handler=get_function_handler_path(
                feature=Feature.EXPENSE,
                action=Action.UPDATE,
            ),
        )

        # DELETE EXPENSE
        expense_delete_function_id = get_function_name(
            name=Feature.EXPENSE.value,
            feature=Feature.EXPENSE,
            action=Action.DELETE,
        )
        self.expense_delete_function = _lambda.Function(
            self,
            expense_delete_function_id,
            function_name=expense_delete_function_id,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset(FUNCTION_CODE_ROOT_PATH),
            handler=get_function_handler_path(
                feature=Feature.EXPENSE,
                action=Action.DELETE,
            ),
        )

        # LIST EXPENSES
        expense_list_function_id = get_function_name(
            name=Feature.EXPENSE.value,
            feature=Feature.EXPENSE,
            action=Action.LIST,
        )
        self.expense_list_function = _lambda.Function(
            self,
            expense_list_function_id,
            function_name=expense_list_function_id,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset(FUNCTION_CODE_ROOT_PATH),
            handler=get_function_handler_path(
                feature=Feature.EXPENSE,
                action=Action.LIST,
            ),
            layers=[self.python_layer],
            role=self.create_function_role(
                f"{Feature.EXPENSE.value}-{Action.LIST.value}",
                [database_stack.reader_policy],
            ),
            environment=self.GLOBAL_ENVIRONMENT,
        )

    def create_layer(self):
        current_dir = os.path.dirname(__file__)
        layers_dir = os.path.join(current_dir, "..", "..", "..", "layers", "python.zip")
        self.python_layer = _lambda.LayerVersion(
            self,
            get_layer_name("python"),
            code=_lambda.Code.from_asset(layers_dir),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_12],
            layer_version_name=get_layer_name("python"),
        )

    def create_function_role(
        self, name: str, policies: list[_iam.PolicyStatement]
    ) -> _iam.Role:
        default_role_name = get_function_role_name(name)
        role = _iam.Role(
            self,
            default_role_name,
            assumed_by=_iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name=default_role_name,
        )
        role.add_to_policy(
            _iam.PolicyStatement(
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                ],
                resources=["*"],
            )
        )
        for policy in policies:
            role.add_to_policy(policy)
        return role
