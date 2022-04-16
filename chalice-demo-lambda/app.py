from chalice import Chalice

app = Chalice(app_name='chalice-demo-lambda')


@app.lambda_function()
def chalice_demo_lambda_function(event, context):
    # Anything you want here.
    return {"demo_lambda_key": "this is a message from test chalice demo lambda function. hello world!"}
