import json
import base64
import boto3
import re

print("Loading Function In")

def my_function3(event, context):
    # TODO implement
    print(event)
    file_content = base64.b64decode(event['body']).decode('utf-8')
    print(file_content)
    bucket_name = event["pathParameters"]["bucket-name"]
    print(bucket_name)
    file_content_match = re.search(r'filename="[^"]+"\r\nContent-Type: [^\r\n]+\r\n\r\n(.*?)\r\n------WebKitFormBoundary', file_content, re.DOTALL)
    contents = file_content_match.group(1) if file_content_match else None
    object_match = re.search(r'name="object_name"\r\n\r\n(.*?)\r\n', file_content, re.DOTALL)
    object_name = object_match.group(1) if object_match else None
    print("Contents:", contents)
    print("Object Name:", object_name)
    s3_client = boto3.client('s3')

    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_name,  
        Body=contents  
    )
    return {
        'statusCode': 201,
        'body': json.dumps({"contents": contents})
    }
