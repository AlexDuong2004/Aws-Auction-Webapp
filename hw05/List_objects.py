import json
import boto3
print("Loading Function In")

def my_function2(event, context):
    # TODO implement
    print(event)
    bucket_name = event["pathParameters"]["bucket-name"]
    s3 = boto3.client("s3")
    query = s3.list_objects_v2(Bucket=bucket_name)
    objects = query.get("Contents", [])
    object_keys = [obj["Key"] for obj in objects] if objects else []

    return {
        'statusCode': 200,
        'body': json.dumps({"Objects": object_keys})
    }

