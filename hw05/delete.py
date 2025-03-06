import json
import base64
import boto3

print("Loading Function In")

def my_function4(event, context):
    # TODO implement
    print(event)
    bucket_name = event["pathParameters"]["bucket-name"]
    print(bucket_name)
    object_name = event["pathParameters"]["object_name"]
    print(object_name)
    s3 = boto3.client('s3')
    s3.delete_object(Bucket=bucket_name, Key=object_name)
    return {
        'statusCode': 200,
        'body': json.dumps('Deleted the object')
    }

