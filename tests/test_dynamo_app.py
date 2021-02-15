"""This test script runs tests agains the dynamoDB app"""
import os
import sys

import pytest
from botocore.stub import ANY, Stubber

SRC_PATH = os.path.join('..', 'lambda')
module_path = os.path.realpath(
    os.path.join(os.path.dirname(__file__),SRC_PATH)
)
sys.path.append(module_path)

TEST_MODULE = 'dynamo_app'

@pytest.fixture(scope="function",name="ddb_stub")
def ddb_stubber():
    """This stubs out the dynamodb call"""
    test_module = __import__(TEST_MODULE)
    ddb_stub = Stubber(test_module.Table.meta.client)
    ddb_stub.activate()
    yield ddb_stub
    ddb_stub.deactivate()

def test_user_exists(ddb_stub):
    """This test is the get_user method when the user exists in the table"""
    test_module = __import__(TEST_MODULE)

    user_id = 'user123'
    get_item_params = {'TableName': ANY,
                       'Key': {'id': user_id}}
    get_item_response = {'Item': {'id': {'S': user_id},
                                  'name': {'S': 'Spam'}}}
    ddb_stub.add_response('get_item', get_item_response, get_item_params)

    result = test_module.get_user(user_id)
    assert result.get('id') == user_id
    ddb_stub.assert_no_pending_responses()

def test_user_missing(ddb_stub):
    """This test is the get_user method when the user does not
    exist in the table"""
    test_module = __import__(TEST_MODULE)

    user_id = 'user123'
    get_item_params = {'TableName': ANY,
                       'Key': {'id': user_id}}
    get_item_response = {}
    ddb_stub.add_response('get_item', get_item_response, get_item_params)

    result = test_module.get_user(user_id)
    assert result is None
    ddb_stub.assert_no_pending_responses()
