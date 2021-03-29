import os
import logging
import strava_setup
from cfnresponse import send, SUCCESS

logger = logging.getLogger()
logger.setLevel(logging.INFO)

callback_url = os.environ['CALLBACK_URL']
region = os.environ['AWS_REGION']

def lambda_handler(event, context):

    responseData= {}
    responseStatus="SUCCESS"

    try: 
        if event['RequestType'] == 'Create':
            #create_sub(callback_url)
            send(event, context, SUCCESS)
            print("Received Create event: " + json.dumps(event, indent=2))
            print("Doing nowt for now")
            return
        
        elif event['RequestType'] == 'Update':
            # do nothing
            send(event, context, SUCCESS)
            print("Received Update event: " + json.dumps(event, indent=2))
            print("Doing nowt for now")
            return        

        else event['RequestType'] == 'Delete':
            # delete sub
            send(event, context, SUCCESS)
            print("Received Delete event: " + json.dumps(event, indent=2))
            print("Doing nowt for now")
            return

    except Exception as e:
        print(e)
        responseData = {'Failed': 'CF Failed.'}
        responseStatus="FAILED"
        cfnresponse.send(event, context, cfnresponse.FAILED, responseData) 


def create_sub(callback_url):
'''
    # pulls API creds from AWS SM with hardcoded secret name for now
    strava_creds = strava_setup.get_api_creds(strava_creds) 

    # Create Subscription using strava_creds
    subscription_id = strava_setup.strava_sub_creator(strava_creds, callback_url)
    
    logger.info(f'Strava Subscription ID = {subscription_id}')

    - handle subscription
    - auth app
    - make initial get to test
'''

def delete_sub():
'''
    - call remove sub
'''