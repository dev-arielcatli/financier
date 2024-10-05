from http import HTTPMethod

import aws_cdk as cdk
from aws_cdk import aws_apigateway as _apigateway
from constructs import Construct
from shared.models.features import Feature
from shared.models.urls import EXPENSE_ID
from shared.utils.naming import get_api_name, get_deployment_name, get_stage_name
from stacks.functions.functions_stack import FunctionsStack


class APIGatewayStack(cdk.Stack):
    def __init__(
        self, scope: Construct, id: str, functions_stack: FunctionsStack, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        api_name = get_api_name(Feature.ROOT.value)
        self.root_api = _apigateway.LambdaRestApi(
            self,
            api_name,
            rest_api_name=api_name,
            handler=functions_stack.fastapi_function,
            deploy=False,
            proxy=True,
            # TODO: Update this when we have a domain
            default_cors_preflight_options=_apigateway.CorsOptions(
                allow_origins=_apigateway.Cors.ALL_ORIGINS,
                allow_methods=_apigateway.Cors.ALL_METHODS,
            ),
        )

        self.main_api = self.root_api.root.add_resource("api")
        self.main_api.add_proxy(
            default_integration=_apigateway.LambdaIntegration(
                functions_stack.fastapi_function
            )
        )

        # DEPLOYMENTS
        stage_name = get_stage_name()
        _apigateway.Deployment(
            self,
            get_deployment_name(),
            stage_name=stage_name,
            retain_deployments=True,
            api=self.root_api,
        )
