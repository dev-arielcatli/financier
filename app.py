#!/usr/bin/env python3

import aws_cdk as cdk

from shared.utils.naming import (
    get_api_gateway_stack_name,
    get_database_stack_name,
    get_functions_stack_name,
)
from stacks.apigateway.api_gateway_stack import APIGatewayStack
from stacks.database.database_stack import DatabaseStack
from stacks.functions.functions_stack import FunctionsStack

app = cdk.App()

database_stack = DatabaseStack(app, get_database_stack_name())
functions_stack = FunctionsStack(app, get_functions_stack_name(), database_stack=database_stack)
APIGatewayStack(app, get_api_gateway_stack_name(), functions_stack=functions_stack)

app.synth()
