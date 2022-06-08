from aws_cdk import (
    Stack,
    aws_secretsmanager as secretsmanager,
    SecretValue as SecretValue,
)
from constructs import Construct
from aws_cdk import aws_events as events


class APIEndpoints(Stack):

    def __init__(
                    self, 
                    scope: Construct, 
                    construct_id: str,
                    **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        self.API_PREFIX = "TestAPI"
        self.API_URL = "https://webhook.site/d2062f94-8283-4327-ba52-355d943bc20e"

        api_connection = events.Connection(
                                                self,
                                                f"{self.API_PREFIX}_API_Connection",
                                                authorization=events.Authorization.api_key(
                                                    "Authorization",
                                                    SecretValue.unsafe_plain_text('Bearer: dummyPassword'),
                                                    ),
                                                description=f"{self.API_PREFIX} dev Connection with Bearer API Authorization Token"
                )
        self.api_destination = events.ApiDestination(
                                                self,
                                                f"{self.API_PREFIX} dev API for Braze",
                                                connection=api_connection,
                                                endpoint=self.API_URL,
                                                description=f"API connection for {self.API_PREFIX} with Bearer API Authorization Token"
                )
