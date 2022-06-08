from aws_cdk import (
    Stack, 
    Duration
)
from constructs import Construct
from aws_cdk import aws_events as events

class EventBus(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.EVENT_BUS_PREFIX = "TestEvent"
        self.EVENTBRIDGE_ARCHIVE_RETENTION_DAYS = 28
        self.eventBusName = f"{self.EVENT_BUS_PREFIX}-eventBus"
        self.eventBusArchiveName = f"{self.EVENT_BUS_PREFIX}-full-archive"

        self.eventBus = events.EventBus(
                                            scope=self, 
                                            id=self.eventBusName, 
                                            event_bus_name=self.eventBusName,
                                            )
        self.eventArchive = self.eventBus.archive(
                                            id=self.eventBusArchiveName,
                                            archive_name=self.eventBusArchiveName,
                                            description=f"Archive of all events from {self.eventBusName}",
                                            event_pattern=events.EventPattern(
                                                account=[Stack.of(self).account]
                                            ),
                                            retention=Duration.days(self.EVENTBRIDGE_ARCHIVE_RETENTION_DAYS)
)
