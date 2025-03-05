import json
import base64
import boto3

print("Loading Function In")

def my_function3(event, context):
    # TODO implement
    print(event)
    file_content = base64.b64decode(event['body-json']['body'])
    print(file_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
