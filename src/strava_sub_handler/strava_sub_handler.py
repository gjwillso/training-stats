"""
Returns Challenge Response on Callback URL
"""

import logging
import json
import urllib3

http = urllib3.PoolManager()

# Configure logging
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def lambda_handler(event, context):
    '''
    Webhook Subscription Handler.
    '''

    event_json = json.dumps(event['queryStringParameters'])

    LOGGER.info('Strava Subscription Handler Starting...')
    LOGGER.info(f"Recieved Event Query Params...{event_json}")

    if event['queryStringParameters']['hub.verify_token'] == 'STRAVA':

        responseObject = {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({"hub.challenge": event['queryStringParameters']['hub.challenge']})
        }

        LOGGER.info(f"Sending Back Hub Challenge ID...{responseObject}")

        return responseObject
    
    else:
        LOGGER.info("Invalid Request")