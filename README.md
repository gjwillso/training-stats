## Strava Training App

Simple App to track training progress

## package with
aws cloudformation package --template-file ./template.yaml --s3-bucket training-stats --output-template-file packaged.template.yaml

## deploy with 
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

