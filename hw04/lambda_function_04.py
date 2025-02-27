"""Python Function for the lambda"""
import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("hw04-ald21039-1")


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print(event)
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    name = event['Records'][0]['s3']['object']['key']
    #print(name)
    bucket_arn = event['Records'][0]['s3']['bucket']['arn']
    #print(bucket_arn)
    size = event['Records'][0]['s3']['object']['size']
    #print(size)
    upload_time = event['Records'][0]['eventTime']
    #print(upload_time)
    etag = event['Records'][0]['s3']['object']['eTag']
    #print(etag)
    try:
        database_info = {
            "file_name": name,
            "file_size": size,
            "upload_time": upload_time,
            "file_etag": etag,
            "bucket_arn": bucket_arn
        }
        print(database_info)
        table.put_item(Item=database_info)
        return database_info
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
              

