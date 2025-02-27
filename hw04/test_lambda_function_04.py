"""Testing the lambda function with DynamoDB"""
import time
import logging
import os
import boto3
from botocore.exceptions import ClientError

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket from hw03."""
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def dynamo_value(file_name):
    """Retrieves an item from DynamoDB using filename"""
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("hw04-ald21039-1")
    response = table.get_item(Key={"file_name": file_name})
    return response.get("Item")


def test_lambda_function():
    """Tests the first dummy file"""
    repo_root = os.getcwd()
    file_path1 = os.path.join(repo_root, 'hw04', 'pytest_files', 'dummyfile1.txt')
    invalid_query = dynamo_value('dummyfile1.txt')
    assert invalid_query is None
    upload_file(file_path1, 'hw04-ald21039-1')
    time.sleep(5)
    valid_query = dynamo_value('dummyfile1.txt')
    assert valid_query is not None
    assert valid_query["file_name"] == 'dummyfile1.txt'
    assert 'upload_time' in valid_query
    assert 'file_etag' in valid_query 
    assert 'file_size' in valid_query
    assert valid_query['bucket_arn'] == 'arn:aws:s3:::hw04-ald21039-1'

def test_lambda_function_2():
    """Tests the second dummy file to make sure it works"""
    repo_root = os.getcwd()
    file_path2 = os.path.join(repo_root, 'hw04', 'pytest_files', 'dummyfile2.txt')
    invalid_query = dynamo_value('dummyfile2.txt')
    assert invalid_query is None
    upload_file(file_path2, 'hw04-ald21039-1')
    time.sleep(5) 
    valid_query = dynamo_value('dummyfile2.txt')
    assert valid_query is not None
    assert valid_query["file_name"] == 'dummyfile2.txt'
    assert 'upload_time' in valid_query
    assert 'file_etag' in valid_query 
    assert 'file_size' in valid_query
    assert valid_query['bucket_arn'] == 'arn:aws:s3:::hw04-ald21039-1'


