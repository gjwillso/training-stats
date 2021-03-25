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


def strava_sub_creator():
    '''
    Post Callback URL to Strava Subscriptions Endpoints to Trigger onboarding Process
    '''

    logger.info('Strava Subscription Creator Starting...')


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


def get_client_secret(secret_name):
    """
    Takes in key name of Strava Client ID stored in AWS Secrets Manager
    """

    sm_client = boto3.client('secretsmanager')

    logger.info("Recieved call to retrieve Strava Client Secret...")

    try:
        client_secret = sm_client.get_secret_value(
            SecretId=secret_name
        )

        secret = client_secret['SecretString']
        return secret

    except ClientError:
        return "Secret Not Found"
