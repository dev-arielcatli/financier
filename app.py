#!/usr/bin/env python3

import aws_cdk as cdk

from financier.stacks.database.database_stack import DatabaseStack

from financier.shared.utils.naming import get_database_stack_name

app = cdk.App()

DatabaseStack(app, get_database_stack_name())

app.synth()
