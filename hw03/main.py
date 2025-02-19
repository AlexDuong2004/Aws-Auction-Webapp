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
        objects = query.get("Contents", [])

        object_keys = [obj["Key"] for obj in objects] if objects else []
        
        return object_keys
    except ClientError as e:
        logging.error(e)
        return []

def download_file(bucket, file_path):
    """Downloads an object from a particular bucket"""
    config = 

    return

if __name__ == "__main__":
    current_bucket = None  

    while True:
        menu_input = input(
            "Select 'q' to quit, 's' to select a bucket, 'u' to upload to a bucket, "
            "'lo' to list objects in a bucket, 'd' to download: "
        ).strip().lower()

        match menu_input:
            case "q":
                break

            case "s":
                current_bucket, bucket_list = select_bucket()
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

            case _:  
                print("Invalid option, please try again.")

