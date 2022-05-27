from chalice import Chalice
import boto3
import json

app = Chalice(app_name='wq-chalice-python-demo')
sns_client = boto3.client('sns')
sqs_client = boto3.client("sqs")

@app.lambda_function()
def chalice_demo_lambda_function(event, context):
    # get this notification json from Segment, production event
    notification = '''
        {
            "anonymousId": null,
            "context": {
                "library": {
                    "name": "analytics-python",
                    "version": "1.4.0"
                },
                "userAgent": "ResQFMv2/14808 CFNetwork/1331.0.7 Darwin/21.4.0"
            },
            "event": "ResqReviewActivityStarted",
            "integrations": {
                "HubSpot": true
            },
            "messageId": "0cf91f4f-5a32-40e3-b0c8-a81b0bab6ab3",
            "originalTimestamp": "2022-05-25T01:59:01.319060+00:00",
            "properties": {
                "activity_id": 1901926,
                "activity_override": false,
                "application": "facility_app",
                "email": "nick@parkerrestaurantgroup.com",
                "path": null,
                "review_type": "FINDING_VENDOR",
                "work_order_id": 134091
            },
            "receivedAt": "2022-05-25T01:59:01.956Z",
            "sentAt": "2022-05-25T01:59:01.711Z",
            "timestamp": "2022-05-25T01:59:01.563Z",
            "type": "track",
            "userId": "9868",
            "writeKey": "KcsS7B5niuXlTkJVn6BFf6qHAekG05Rk"
        }
    '''

    response = sns_client.publish(
        TargetArn="arn:aws:sns:us-east-1:176982589840:wq-demo-t0",
        Message=json.dumps({'default': notification}),
        MessageStructure='json'
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
