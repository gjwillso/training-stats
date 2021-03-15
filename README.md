## Strava Training App

Simple App to track training progress

## Package with
aws cloudformation package --template-file ./template.yaml --s3-bucket training-stats --output-template-file packaged.template.yaml

## Deploy with 
aws cloudformation deploy --template-file ./packaged.template.yaml --stack-name training-stats --capabilities CAPABILITY_IAM

## Activation Service with Subscription push

curl -X POST https://www.strava.com/api/v3/push_subscriptions \
      -F client_id=<client_id> \
      -F client_secret=<client_secret> \
      -F 'callback_url=http://a-valid.com/url' \
      -F 'verify_token=STRAVA'

This will trigger a callback validation from the Strava Subscription service in the form of a GET request made to the curlback_url provided in the above subscription push.

Example Validation Request
$ GET https://mycallbackurl.com?hub.verify_token=STRAVA&hub.challenge=15f7d1a91c1f40f8a748fd134752feb3&hub.mode=subscribe


## Notes

- Had to manually deploy the strava-sub-handler API via console to take effect.
    Type: AWS::ApiGateway::Deployment - doesn't appear to have run

- Once the subscription has been setup, I had to accept an auth request via the strava console with the correct scope:
  https://www.strava.com/oauth/authorize?client_id=11111&response_type=code&redirect_uri=http://localhost&approval_prompt=force&scope=activity:read_all

- Then take the returned code an request a refresh and bearer token 
  curl -X POST https://www.strava.com/api/v3/oauth/token -d client_id=11111 -d client_secret=secret -d code=6cfc52194c8047eaf007cf56d3a6ef5356846637 -d grant_type=authorization_code

- Then actually make a call to the API to enable the end to end webhook flow
  
  curl -G https://www.strava.com/api/v3/athlete -H "Authorization: Bearer replace_with_bearer_token"
  curl -G "https://www.strava.com/api/v3/athlete/activities?access_token=replace_with_bearer_token"


- Saved Mapping template:

{ 
    "TableName": "table-name",
    "Item": {
        "object_id": {"N": $input.json('$.object_id')},
        "event_time": {"N": $input.json('$.event_time')}
    }
}