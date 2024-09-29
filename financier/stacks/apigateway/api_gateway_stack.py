from http import HTTPMethod

import aws_cdk as cdk
from aws_cdk import aws_apigateway as _apigateway
from constructs import Construct

from financier.shared.models.features import Feature
from financier.shared.utils.naming import (
    get_api_name,
    get_deployment_name,
    get_stage_name,
)
from financier.stacks.functions.functions_stack import FunctionsStack


class APIGatewayStack(cdk.Stack):
    def __init__(
        self, scope: Construct, id: str, functions_stack: FunctionsStack, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        api_name = get_api_name(Feature.DEFAULT.value)
        self.root_api = _apigateway.LambdaRestApi(
            self,
            api_name,
            rest_api_name=api_name,
            handler=functions_stack.expense_main_function,
            deploy=False,
            # TODO: Update this when we have a domain
            default_cors_preflight_options=_apigateway.CorsOptions(
                allow_origins=_apigateway.Cors.ALL_ORIGINS,
                allow_methods=_apigateway.Cors.ALL_METHODS,
            ),
        )

        # /expense
        expense_resource = self.root_api.root.add_resource(Feature.EXPENSE.value)
        expense_resource.add_method(
            HTTPMethod.GET,
            _apigateway.LambdaIntegration(
                functions_stack.expense_list_function,
            ),
        )
        expense_resource.add_method(
            HTTPMethod.POST,
            _apigateway.LambdaIntegration(
                functions_stack.expense_create_function,
            ),
        )

        # /expense/{id}
        identified_expense_resource = expense_resource.add_resource("{id}")
        identified_expense_resource.add_method(
            HTTPMethod.GET,
            _apigateway.LambdaIntegration(
                functions_stack.expense_get_function,
            ),
        )
        identified_expense_resource.add_method(
            HTTPMethod.PUT,
            _apigateway.LambdaIntegration(
                functions_stack.expense_update_function,
            ),
        )
        identified_expense_resource.add_method(
            HTTPMethod.DELETE,
            _apigateway.LambdaIntegration(
                functions_stack.expense_delete_function,
            ),
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
