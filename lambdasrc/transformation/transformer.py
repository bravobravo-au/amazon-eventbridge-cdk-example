import os
import boto3
import json
from datetime import datetime

def main(event, context):
    eventBridgeSource = event['source']
    eventBridgeDetail = event['detail']
    eventrBusARN = os.environ.get('EVENT_BUS_ARN','')
    
    eventBridgeClient = boto3.client('events')


    eventBridgeDetailOUT = {
            "new_name": eventBridgeDetail['name'],
            "utc_timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        }

    
    eventBridgeSourceOUT = 'com.testing.test.003'

    eventBridgeResponseOUT = eventBridgeClient.put_events(
    Entries=[
            {
                'Source': eventBridgeSourceOUT,
                'DetailType': eventBridgeSourceOUT,
                'Detail': json.dumps(eventBridgeDetailOUT),
                'EventBusName': eventrBusARN,
            },
        ],
    )

