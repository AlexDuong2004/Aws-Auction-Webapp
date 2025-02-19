import logging
import boto3
from botocore.exceptions import ClientError
import os

def select_bucket():
    """Prompts the user to select a valid S3 bucket and returns the selection."""
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    bucket_names = {bucket["Name"] for bucket in response.get("Buckets", [])}
    if not bucket_names:
        print("No available buckets found.")
        return None
    print("Existing buckets:")
    for name in bucket_names:
        print(f"- {name}")
    while True:
        selected_bucket = input("Type the bucket you'd like to use: ").strip()
        if selected_bucket in bucket_names:
            return selected_bucket
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

if __name__ == "__main__":
    current_bucket = None  
    while True:
        menu_input = input("Select 'q' to quit, 's' to select a bucket, select 'u' to upload to a bucket: ").strip().lower()
        if menu_input == "q":
            break
        elif menu_input == "s":
            current_bucket = select_bucket()
            print(f"Current bucket set to: {current_bucket}")
        elif menu_input == "u":
            if current_bucket is None:
                print("No bucket selected please select a bucket")
            else:
                file_path = input("Enter the path to your file: ").strip()
                name_of_file = input("Enter a name for the file or press enter to skip: ").strip()
                upload_file(file_path, current_bucket, name_of_file)

