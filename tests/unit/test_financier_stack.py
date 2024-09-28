import aws_cdk as core
import aws_cdk.assertions as assertions

from financier.financier_stack import FinancierStack

# example tests. To run these tests, uncomment this file along with the example
# resource in financier/financier_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FinancierStack(app, "financier")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
