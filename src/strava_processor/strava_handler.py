import json
import boto3
from cfnresponse import send, SUCCESS
from botocore.exceptions import ClientError
#import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

print('Strava Grabber Activated...')


def lambda_handler(event, context):

    logger.info(f"Recieved New Activity Notification {json.dumps(event)}")

    response_object = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'returning body': event})
    }

    logger.info(f"Sending Back 200...{response_object}")

    return response_object


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

'''