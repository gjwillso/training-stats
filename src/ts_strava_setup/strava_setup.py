"""
Modules for working with the Strava API
"""

import logging
import json
import requests
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def strava_sub_creator(strava_creds, callback_url):
    '''
    Post Callback URL to Strava Subscriptions Endpoints to Trigger onboarding process
    '''

    logger.info('Strava Subscription Creator Starting...')

    payload = {
     'client_id': '31306',
     'client_secret': 'e173c7c091fc8b829b1e76d11f5d6282200c4341',
     'callback_url': 'https://iv33ccvs9g.execute-api.eu-west-1.amazonaws.com/v1/strava',
     'verify_token': 'STRAVA'
    }

    response = requests.post('https://www.strava.com/api/v3/push_subscriptions', data=payload)

    logger.info('Strava Subscription Request Sent...')

    return response


def strava_sub_handler(event):
    ''' 
    Webhook Subscription Handler. 
    '''    

    event_json = json.dumps(event['queryStringParameters'])

    logger.info('Strava Subscription Handler Starting...')
    logger.info(f"Recieved Event Query Params...{event_json}")

    if event['queryStringParameters']['hub.verify_token'] == 'STRAVA':

            responseObject = {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': {'hub.challenge': event['queryStringParameters']['hub.challenge']}
            }

            logger.info(f"Sending Back Hub Challenge ID...{responseObject}")

            return responseObject
    else:
        logger.info("Invalid Request")


def get_api_creds(secret_name):
    """
    Pulls Strava Client ID & Client Secret stored in AWS Secrets Manager
    """

    sm_client = boto3.client('secretsmanager')

    logger.info("Recieved call to retrieve Strava Creds...")

    try:
        client_secret = sm_client.get_secret_value(
            SecretId=secret_name
        )

        secret = client_secret['SecretString']
        return secret

    except ClientError:
        return "Secret Not Found"
