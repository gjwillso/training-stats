import json
import boto3
from botocore.exceptions import ClientError
#import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

print('Strava Grabber Activated...')


def lambda_handler(event, context):

    logger.info(f"Recieved New Activity Notification {json.dumps(event)}")

    responseObject = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'returning body': event})
    }

    logger.info(f"Sending Back 200...{responseObject}")

    return responseObject


'''
    tokendata = json.loads(get_secret())   
    token = (tokendata['strava-token'])
    headers = {'Authorization': "Bearer {0}".format(token)}

    webhook_body = app.current_request.json_body

    if webhook_body['aspect_type'] == 'create':
        print (webhook_body)
        logger.info("Processing New Strava Actvity...")
        id  = webhook_body['object_id']
        r = requests.get("https://www.strava.com/api/v3/activities/{0}".format(id), headers=headers)
        activity = r.json()
        print (activity)

        if activity["type"] == 'Run':
            logger.info("Copying Running Activity to S3...")
            s3 = boto3.resource('s3')
            s3.Object('run-stats', "strava-run-stats.json").put(Body=json.dumps(activity))
    
        elif activity["type"] == 'Ride':
            logger.info("Copying Cycling Activity to S3...")
            s3 = boto3.resource('s3')
            s3.Object('ride-stats', "strava-ride-stats.json").put(Body=json.dumps(activity))
    
        else: 
            logger.info("Dropping Random Activity...")
            # need to handle other sports
    else:
        logger.info("Dropping Update / Delete Activity for now...")

def get_secret():
    secret_name = "strava-token"
    region_name = "eu-west-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e

    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])

'''
