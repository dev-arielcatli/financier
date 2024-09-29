#!/usr/bin/env python3

import aws_cdk as cdk

from financier.shared.utils.naming import (
    get_api_gateway_stack_name,
    get_database_stack_name,
    get_functions_stack_name,
)
from financier.stacks.apigateway.api_gateway_stack import APIGatewayStack
from financier.stacks.database.database_stack import DatabaseStack
from financier.stacks.functions.functions_stack import FunctionsStack

app = cdk.App()

DatabaseStack(app, get_database_stack_name())
functions_stack = FunctionsStack(app, get_functions_stack_name())
APIGatewayStack(app, get_api_gateway_stack_name(), functions_stack=functions_stack)

app.synth()
