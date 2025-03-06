import json
import boto3

print("Loading Function In")

def my_function1(event, context):
    # TODO implement
    print(event)
    client = boto3.client("s3")
    information = client.list_buckets()
    bucket_names = []
    for i in information.get("Buckets", []):
        bucket_names.append(i["Name"])
    print(f"bucket names: {bucket_names}")
    return {
            "statusCode": 200,
            "body": json.dumps({"buckets": bucket_names})
        }
