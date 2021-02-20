import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

print('Strava Subscription Handler Starting...')

def lambda_handler(event, context):
    ''' 
    Webhook Subscription Handler. 
    '''    
    logger.info(f"Recieved Event Query Params...{json.dumps(event['queryStringParameters'])}")

    if event['queryStringParameters']['hub.verify_token'] == 'STRAVA-GREG':      
       
            responseObject = {
                "statusCode": 200,
                "body": json.dumps({'hub.challenge': event['queryStringParameters']['hub.challenge']})
            }

            logger.info(f"Sending Back Hub Challenge ID...{responseObject}")
            
            return responseObject
    else:
        logger.info("Invalid Request")