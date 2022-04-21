from chalice import Chalice
import boto3
import json

app = Chalice(app_name='wq-chalice-python-demo')
sns_client = boto3.client('sns')
sqs_client = boto3.client("sqs")

@app.lambda_function()
def chalice_demo_lambda_function(event, context):
    # this is an example for publish an event to sns
    notification = "Here is the SNS notification for Lambda function."
    response = sns_client.publish(
        TargetArn="arn:aws:sns:us-east-1:176982589840:wq-demo-t0",
        Message=json.dumps({'default': notification}),
        MessageStructure='json'
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

# Listen to SNS and SQS

# @app.on_sns_message(topic='SNSTopicName')
# def handle_sns_message(event):
#     app.log.debug("Received message with subject: %s, message: %s",
#                   event.subject, event.message)

# @app.on_sqs_message(queue=INPUT_QUEUE_NAME)
# def on_event(event):
#     return {'hello': 'world'}