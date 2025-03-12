'''
These are methods using the S3 Resource API. Feel free to switch to use
the S3 Client API
'''
import boto3

def create_client():
    '''Create the S3 client'''   
    # Feel free to switch to the Client API instead of using the Resouce API 
    return boto3.client('s3')

def list_objects(bucket_name):
    '''Returns a list of objects in the bucket'''
    # TODO: Use boto3 to get the list of objects in the bucket_name
    s3 = create_client()
    query = s3.list_objects_v2(Bucket=bucket_name)
    if "Contents" not in query:
            return []
    objects = query.get("Contents", [])
    object_keys = []
    if objects == None:
        return object_keys
    for obj in objects:
        object_metadata = {
            'Name': obj['Key'], 
            'Size': obj['Size'],  
            'LastModified': obj['LastModified'] 
        }
        object_keys.append(object_metadata)
    return object_keys

def upload_file_to_s3(file, bucket_name):
    '''Uploads a file to S3'''
    s3 = create_client()
    # TODO: Upload the file to the given bucket_name
    name = file.filename
    s3.upload_fileobj(file, bucket_name, name)
    return

def generate_thumbnail(bucket_name, object_key):
    '''Generate a pre-signed URL for accessing an object in S3'''
    s3 = create_client()
    thumbnail = s3.get_object(Bucket=bucket_name, Key=object_key)
    image_data = thumbnail['Body'].read()
    return image_data


if __name__ == "__main__":
    # You can unit test your methods before trying to integrate with the HTML code
    l = list_objects("hw06-ald21039-1")
    print(l)
    print(generate_thumbnail("hw06-ald21039-1", 's3.jpg'))