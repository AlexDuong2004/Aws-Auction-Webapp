import logging
import boto3
from botocore.exceptions import ClientError
import os

def select_bucket():
    """Prompts the user to select a valid S3 bucket and returns the selection and the list of buckets."""
    bucket_list = []
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    bucket_names = {bucket["Name"] for bucket in response.get("Buckets", [])}
    if not bucket_names:
        print("No available buckets found.")
        return None
    print("Existing buckets:")
    for name in bucket_names:
        bucket_list.append(name)
        print(f"- {name}")
    while True:
        selected_bucket = input("Type the bucket you'd like to use: ").strip()
        if selected_bucket in bucket_names:
            return selected_bucket, bucket_list
        print("Invalid bucket name. Please enter a valid bucket from the list.")

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket."""
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def list_objects(bucket):
    """List all the objects in a bucket"""
    s3 = boto3.client("s3")
    try:
        query = s3.list_objects_v2(Bucket=bucket)
        if "Contents" not in query:
            return []
        objects = query.get("Contents", [])
        object_keys = [obj["Key"] for obj in objects] if objects else []
        return object_keys
    except ClientError as e:
        logging.error(e)
        return []

def download_file(bucket, file_path):
    """Downloads an object from a particular bucket"""
    s3 = boto3.client('s3')
    available_objects = list_objects(bucket)
    if not available_objects:
        print("No files found in the bucket.")
        return 
    while True:
        selected_object = input("Select a valid object:").strip()
        if selected_object in available_objects:
            break
        print("Incorrect object please select a valid one: ")
        print(available_objects)
    s3.download_file(bucket, selected_object, file_path)
    return 

def pre_signed_url(bucket):
    """Generates a presigned url for a s3 object"""
    s3_client = boto3.client('s3')
    expiration = 3600
    available_objects = list_objects(bucket)
    if not available_objects:
        print("No files found in the bucket.")
        return 
    while True:
        selected_object = input("Select a valid object:").strip()
        if selected_object in available_objects:
            break
        print("Incorrect object please select a valid one: ")
        print(available_objects)
    try:
        response = s3_client.generate_presigned_url('get_object', 
                                                    Params={'Bucket': bucket,
                                                            'Key': selected_object},
                                                            ExpiresIn= expiration)
    except ClientError as e:
        logging.error(e)
        return None
    
    return response

def list_object_versions(bucket):
    """Retrieve all versions of a specific object in an S3 bucket."""
    s3 = boto3.client('s3')
    available_objects = list_objects(bucket)
    if not available_objects:
        print("No files found in the bucket.")
        return 
    while True:
        selected_object = input("Select a valid object:").strip()
        if selected_object in available_objects:
            break
        print("Incorrect object please select a valid one: ")
        print(available_objects)

    try:
        response = s3.list_object_versions(Bucket=bucket, Prefix=selected_object)

        if "Versions" not in response:
            print("No version found")
            return []

        return response["Versions"]  

    except ClientError as e:
        print(f"Error retrieving object versions: {e}")
        return []
        

if __name__ == "__main__":
    current_bucket = None  

    while True:
        menu_input = input(
            "Select 'q' to quit, 's' to select a bucket, 'u' to upload to a bucket, "
            "'lo' to list objects in a bucket, 'd' to download, 'psu' for a presigned "
            "url :"
        ).strip().lower()

        match menu_input:
            case "q":
                break

            case "s":
                current_bucket, bucket_list = select_bucket()
                if current_bucket:
                    print(f"Current bucket set to: {current_bucket}")

            case "u":
                if current_bucket is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    file_path = input("Enter the path to your file: ").strip()
                    name_of_file = input("Enter a name for the file or press enter to skip: ").strip()
                    upload_file(file_path, current_bucket, name_of_file)

            case "lo":
                if current_bucket is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    object_list = list_objects(current_bucket)
                    print(object_list)

            case "d":
                if current_bucket is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    path_file = input("Enter the path to your file: ").strip()
                    download_file(current_bucket, path_file)

            case "psu":
                if current_bucket is None:
                    print("No bucket selected, please select a bucket.")
                else: 
                    url = pre_signed_url(current_bucket)
                    print(f"Your url is: {url}")

            case "v":
                if current_bucket is None:
                    print("No bucket selected, please select a bucket.")
                else: 
                    version_info = list_object_versions(current_bucket)
                    print(version_info)

            case _:  
                print("Invalid option, please try again.")

