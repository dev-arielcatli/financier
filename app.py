#!/usr/bin/env python3

import aws_cdk as cdk

from financier.financier_stack import FinancierStack
from financier.stacks.database.database_stack import DatabaseStack


app = cdk.App()

FinancierStack(app, "FinancierStack")
DatabaseStack(app, "DatabaseStack")

app.synth()
