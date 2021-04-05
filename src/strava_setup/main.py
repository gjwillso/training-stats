"""
Training Stats Strava Setup
"""

import os
import logging
import boto3
import cfnresponse
import strava_setup

# Configure logging
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Lambda Entry Point
    """

    LOGGER.info(f"Boto3 version: {boto3.__version__}")
    LOGGER.info(f'Received Event {event}')

    status = cfnresponse.FAILED
    data = {}

    request_type = event['RequestType']
    if request_type == 'Delete':
        status, data = delete(event)
    elif request_type == 'Update':
        #status, data = update(event)
        status, data = create(event)
    elif request_type == 'Create':
        status, data = create(event)

    else:
        status = cfnresponse.FAILED
        LOGGER.error('No managed event found, request_type {}'.format(request_type))
        data = {'error': 'No managed event found, request_type {}'.format(request_type)}

    cfnresponse.send(event=event, context=context, responseStatus=status, responseData=data)


def create(event):
    """
    Triggers the creation of API Subscription and handles challenge response
    """

    data = {}
    status = cfnresponse.FAILED

    LOGGER.info(f'Received CREATE Event {event}')

    # Bring in required Env Vars
    region_name = os.getenv('Region')
    callback_url = os.getenv('CallBack_Url')
    secret_name = os.getenv('Secret_Name')

    try:
        # Obtain creds to auth against the subscriptions API
        api_creds = strava_setup.get_api_creds(secret_name, region_name)

        # Call Strava Subscription Creator
        subscription_id = strava_setup.strava_sub_creator(api_creds, callback_url)

        LOGGER.info(f'Sucessfully Subscribed Strava App with ID: {subscription_id}')
        LOGGER.info('Sending back SUCCESS')

        status = cfnresponse.SUCCESS

    except BaseException as e:
        LOGGER.exception(e)
        status = cfnresponse.FAILED

    finally:
        return status, data


def update(event):
    data = {}
    status = cfnresponse.FAILED

    LOGGER.info('Received UPDATE Event {}'.format(event))

    try:        
        #Discover Central DNS account VPC-ID
        #central_vpc_id = get_central_dns_local_vpc_id(central_dns_acct, central_dns_vpc_ssm)

        LOGGER.info(f'Doing nowt with Event {event}')

        status = cfnresponse.SUCCESS

    except BaseException as e:
        LOGGER.exception(e)
        status = cfnresponse.FAILED
    
    finally:
        return status, data


def delete(event):
    data = {}
    status = cfnresponse.FAILED

    LOGGER.info('Received DELETE Event {}'.format(event))

    try:        
        #Discover Central DNS account VPC-ID
        #central_vpc_id = get_central_dns_local_vpc_id(central_dns_acct, central_dns_vpc_ssm)

        LOGGER.info('doing nowt with Event {}'.format(event))
        
        status = cfnresponse.SUCCESS

    except BaseException as e:
        LOGGER.exception(e)
        status = cfnresponse.FAILED
    
    finally:
        return status, data