"""
This test script checks the training stats strava setup functions
"""
# importing modules, need a cleaner way of doing this
from src.strava_setup.strava_setup import strava_sub_handler
from src.strava_setup.main import create

def test_strava_sub_handler():
    '''Challenge ID should be echoed back in response body '''

    mock_event = {
        "queryStringParameters": {
            "hub.challenge": "15f7d1a91c1f40f8a748fd134752feb3",
            "hub.mode": "subscribe",
            "hub.verify_token": "STRAVA"
        }
    }

    response = strava_sub_handler(mock_event)

    assert response["statusCode"] == 200
    assert response["body"]["hub.challenge"] == mock_event["queryStringParameters"]["hub.challenge"]


# used to mock context for lambda trigger
# class context:
#  def __init__(self, log_stream_name):
#    self.log_stream_name = log_stream_name

def test_create():
    ''' SUCCESS should be sent back - doesn't do alot atm'''

    mock_event = {
            "RequestType": "Create",
            "ResponseURL": "http://pre-signed-S3-url-for-response",
            "StackId": "arn:aws:cloudformation:eu-west-1:123456789012:stack/MyStack/guid",
            "RequestId": "unique id for this create request",
            "ResourceType": "Custom::TestResource",
            "LogicalResourceId": "MyTestResource",
	        "ResourceProperties": {
		        "Region": "eu-test-1",
		        "CallBack_Url": "https://mock.execute-api.eu-west-1.amazonaws.com/v1"
	        }
        }

    response = create(mock_event)

    assert response == ('SUCCESS', {})
