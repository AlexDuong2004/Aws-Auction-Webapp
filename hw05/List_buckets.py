import json
import boto3

print("Loading Function In")

def my_function2(event, context):
    # TODO implement
    print(event)
    client = boto3.client("s3")
    information = client.list_buckets()
    bucket_names = []
    for i in information.get("Buckets", []):
        bucket_names.append(i["Name"])
        
    return {
            "statusCode": 200,
            "body": json.dumps({"buckets": bucket_names})
        }
