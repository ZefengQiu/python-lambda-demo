# Listen to SNS and SQS

# @app.on_sns_message(topic='SNSTopicName')
# def handle_sns_message(event):
#     app.log.debug("Received message with subject: %s, message: %s",
#                   event.subject, event.message)

# @app.on_sqs_message(queue=INPUT_QUEUE_NAME)
# def on_event(event):
#     return {'hello': 'world'}