import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_price_tracker.cdk_price_tracker_stack import CdkPriceTrackerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_price_tracker/cdk_price_tracker_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPriceTrackerStack(app, "cdk-price-tracker")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
