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
    object_keys = [obj["Key"] for obj in objects] if objects else []
    return object_keys

def upload_file_to_s3(file, bucket_name):
    '''Uploads a file to S3'''
    s3 = create_client()
    # TODO: Upload the file to the given bucket_name
    s3.upload_file(file, bucket_name, "placeholder")
    return


if __name__ == "__main__":
    # You can unit test your methods before trying to integrate with the HTML code
    l = list_objects("your-bucket-name-here")
    print(l)