"""
Modules for working with the Strava API
"""

import logging
import json
import urllib3
import boto3
import base64
from botocore.exceptions import ClientError


http = urllib3.PoolManager()

# Configure logging
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def strava_sub_creator(api_creds, callback_url):
    '''
    Post Callback URL to Strava Subscriptions Endpoints to Trigger onboarding process
    '''

    LOGGER.info('Strava Subscription Creator Starting...')

    credentials = json.loads(api_creds)

    response = http.request(
        'POST',
        'https://www.strava.com/api/v3/push_subscriptions',
        fields={
            'client_id': credentials["client_id"],
            'client_secret': credentials["client_secret"],
            'callback_url': callback_url,
            'verify_token': 'STRAVA'
            }
        )

    LOGGER.info(response.data)

    LOGGER.info('Strava Subscription Request Sent...')

    return response.data

def strava_sub_handler(event):
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
                'body': {'hub.challenge': event['queryStringParameters']['hub.challenge']}
            }

            LOGGER.info(f"Sending Back Hub Challenge ID...{responseObject}")

            return responseObject
    else:
        LOGGER.info("Invalid Request")


def get_api_creds(secret_name, region_name):
    """
    Pulls Strava Client ID & Client Secret stored in AWS Secrets Manager
    """

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        LOGGER.info(f"Trying to Retrieve Secret: {secret_name}")

        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        LOGGER.info("Recieved Response")

    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        
        if 'SecretString' in get_secret_value_response:
            LOGGER.info("Secret Inside string response... sending back")
            return get_secret_value_response['SecretString']
        else:
            LOGGER.info("Secret Inside binary response... sending back")
            return base64.b64decode(get_secret_value_response['SecretBinary'])