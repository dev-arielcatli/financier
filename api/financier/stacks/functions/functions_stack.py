import os

import aws_cdk as cdk
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from constructs import Construct
from shared.config import (
    APP_NAME,
    FASTAPI_FUNCTION_CODE_PATH,
    FUNCTION_CODE_ROOT_PATH,
    STAGE,
)
from shared.models.actions import Action
from shared.models.features import Feature
from shared.utils.naming import (
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
        self.create_fastapi_function(database_stack=database_stack)

    def create_fastapi_function(self, database_stack: DatabaseStack):
        fastapi_function_id = get_function_name(
            name="fastapi",
            feature=Feature.FASTAPI,
            action=Action.MAIN,
        )
        self.fastapi_function = _lambda.Function(
            self,
            fastapi_function_id,
            function_name=fastapi_function_id,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset(FUNCTION_CODE_ROOT_PATH),
            handler=FASTAPI_FUNCTION_CODE_PATH,
            layers=[self.python_layer],
            role=self.create_function_role(
                f"{Feature.FASTAPI.value}-{Action.MAIN.value}",
                [database_stack.reader_writer_policy],
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
