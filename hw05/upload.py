import json
import base64
import boto3
import re

print("Loading Function In")

def extract_file_and_object_name(data):
    """Extract file content and object name from multipart body"""
    boundary_match = re.search(r'--[^\r\n]+', data)
    
    if boundary_match:
        boundary = boundary_match.group(0) 
        
        file_content_match = re.search(
            rf'Content-Disposition: form-data; name="file"; filename="[^"]+"\r\nContent-Type: [^\r\n]+\r\n\r\n(.*?)\r\n{re.escape(boundary)}',
            data, re.DOTALL
        )
        
        object_name_match = re.search(
            rf'Content-Disposition: form-data; name="object_name"\r\n\r\n(.*?)\r\n{re.escape(boundary)}',
            data, re.DOTALL
        )
        
        file_content = file_content_match.group(1).strip() if file_content_match else None
        object_name = object_name_match.group(1).strip() if object_name_match else None
        
        return file_content, object_name
    
    return None, None


def my_function3(event, context):
    file_content = base64.b64decode(event['body'])
    print("Decoded body:", file_content)

    file_content, object_name = extract_file_and_object_name(file_content.decode('utf-8'))
    
    if not file_content or not object_name:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing file content or object name'})
        }
    
    bucket_name = event["pathParameters"]["bucket-name"]
    print("Bucket name:", bucket_name)
    print("Object name:", object_name)
    print("File content:", file_content)
    
    s3_client = boto3.client('s3')
    
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_name,  
        Body=file_content 
    )
    
    return {
        'statusCode': 201,
        'body': json.dumps({"file_name": object_name})
    }
