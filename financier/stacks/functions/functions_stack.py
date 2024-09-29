import aws_cdk as cdk
from aws_cdk import aws_lambda as _lambda
from constructs import Construct

from financier.shared.config import FUNCTION_CODE_ROOT_PATH
from financier.shared.models.actions import Action
from financier.shared.models.features import Feature
from financier.shared.utils.naming import get_function_handler_path, get_function_name


class FunctionsStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Expense Functions
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
