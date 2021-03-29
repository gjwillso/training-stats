"""This test script checks the training stats strava setup functions"""

#import pytest
#from botocore.stub import ANY, Stubber

from strava_setup import strava_sub_handler


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
