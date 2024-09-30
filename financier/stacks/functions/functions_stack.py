import aws_cdk as cdk
from aws_cdk import aws_lambda as _lambda
from constructs import Construct

from shared.config import FUNCTION_CODE_ROOT_PATH
from shared.models.actions import Action
from shared.models.features import Feature
from shared.utils.naming import get_function_handler_path, get_function_name, get_layer_name

import os

class FunctionsStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.create_layer()
        self.create_expense_functions()

        
    def create_expense_functions(self):
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
        )

    def create_layer(self):
        current_dir = os.path.dirname(__file__)
        layers_dir = os.path.join(current_dir,  "..", "..", "..", "layers", "python.zip")
        self.python_layer = _lambda.LayerVersion(
            self,
            get_layer_name("python"),
            code=_lambda.Code.from_asset(layers_dir),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_12],
            layer_version_name=get_layer_name("python"),
        )