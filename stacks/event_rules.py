from aws_cdk import (
    Stack, 
    Duration,
    aws_events as events,
    aws_events_targets as targets,
    aws_lambda as aws_lambda
    )
from constructs import Construct

class EventRules(Stack):

    def __init__(
                    self, 
                    scope: Construct, 
                    construct_id: str,
                    eventBus=None,
                    api_destination=None,
                    **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.rulePrefix = 'TestRule'
        
        ruleName = '001'

        message_source = 'com.testing.test.001'
        rule001 = events.Rule(
                                scope=self,
                                id=f'{self.rulePrefix}{ruleName}',
                                rule_name=ruleName,
                                description=f"{self.rulePrefix} Rule: {ruleName}",
                                event_bus=eventBus,
                                event_pattern=events.EventPattern(
                                            source=[message_source]
                                            ),
                    )

        args = {
                'max_event_age': Duration.hours(1),
                'retry_attempts': 3,       
                'api_destination': api_destination,
                'event': events.RuleTargetInput.from_object( {
                                    "testid": events.EventField.from_path('$.detail.id'),

                    } )
                }

        ruleTarget001 = targets.ApiDestination( **args )
        rule001.add_target( ruleTarget001 )


        lambda_args = {
                'scope': self,
                'id' : f'{self.rulePrefix}TransformerLambda',
                'handler': "transformer.main",
                'code': aws_lambda.Code.from_asset( "./lambdasrc/transformation" ),
                'runtime': aws_lambda.Runtime.PYTHON_3_9,
                'memory_size': 128,
                'timeout': Duration.seconds(30),
                'environment': {
                                "EVENT_BUS_ARN": eventBus.event_bus_arn,
                                },
                }

        createdFunc = aws_lambda.Function(
                    **lambda_args
                    )
        eventBus.grant_put_events_to( createdFunc )
 
        ruleName = '002'
        message_source = 'com.testing.test.002'
        rule002 = events.Rule(
                                scope=self,
                                id=f'{self.rulePrefix}{ruleName}',
                                rule_name=ruleName,
                                description=f"{self.rulePrefix} Rule: {ruleName}",
                                event_bus=eventBus,
                                event_pattern=events.EventPattern(
                                            source=[message_source]
                                            ),
                    )
        args = {
                'max_event_age': Duration.hours(1),
                'retry_attempts': 3,
                'api_destination': api_destination,
                }

        lambdaTarget = targets.LambdaFunction( handler=createdFunc, max_event_age=Duration.hours(1), retry_attempts=3)
        rule002.add_target( lambdaTarget )

        ruleName = '003'
        message_source = 'com.testing.test.003'
        rule003 = events.Rule(
                                scope=self,
                                id=f'{self.rulePrefix}{ruleName}',
                                rule_name=ruleName,
                                description=f"{self.rulePrefix} Rule: {ruleName}",
                                event_bus=eventBus,
                                event_pattern=events.EventPattern(
                                            source=[message_source]
                                            ),
                    )

        args = {
                'max_event_age': Duration.hours(1),
                'retry_attempts': 3,
                'api_destination': api_destination,
                }

        ruleTarget003 = targets.ApiDestination( **args )
        rule003.add_target( ruleTarget003 )

