#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.eventbus import EventBus
from stacks.api_endpoints import APIEndpoints
from stacks.event_rules import EventRules

app = cdk.App()

eventBus = EventBus(app, "EventbusStack",
    env=cdk.Environment(
                account=os.getenv('CDK_DEFAULT_ACCOUNT'),
                region=os.getenv('CDK_DEFAULT_REGION')
                ),
    )

apiEndpoints = APIEndpoints(app, "APIEndpointsStack",
    env=cdk.Environment(
                account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
                region=os.getenv('CDK_DEFAULT_REGION')
                ),
    )

allEventRules = EventRules(app, "EventRuleStack",
    env=cdk.Environment(
                account=os.getenv('CDK_DEFAULT_ACCOUNT'),
                region=os.getenv('CDK_DEFAULT_REGION')
                ),
    eventBus=eventBus.eventBus,
    api_destination=apiEndpoints.api_destination,
    )
app.synth()
