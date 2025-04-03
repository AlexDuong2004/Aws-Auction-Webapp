import json
from datetime import datetime
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("hw07-ald21039-image-metadata")

def metadata_generator(event, context):
    """Creates the metadata"""
    # TODO implement
    print(event)
    record = event.get("Records", [])[0]
    sent_timestamp_ms = int(record["attributes"]["SentTimestamp"])
    modified_date = datetime.utcfromtimestamp(sent_timestamp_ms / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')
    print(f"date: {modified_date}")
    body_str = event["Records"][0]["body"]
    body = json.loads(body_str)
    message_str = body["Message"]
    message = json.loads(message_str)
    file_name = message["Records"][0]["s3"]["object"]["key"]
    file_size = message["Records"][0]["s3"]["object"]["size"]
    print(f"file_name: {file_name}")
    print(f"file_size: {file_size}")
    try:
        database_info = {
            "FileName": file_name,
            "file_size": file_size,
            "modified_date": modified_date,
        }
        print(database_info)
        table.put_item(Item=database_info)
        return database_info
    except Exception as e:
        print(e)
        print('Error')
        raise e
    
