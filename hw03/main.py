"""Does various commands for a s3 bucket that is prompted through command line"""
import logging
import os
import boto3
from botocore.exceptions import ClientError

def bucket_listing():
    """Lists the buckets you are able to use"""
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    bucket_names = {bucket["Name"] for bucket in response.get("Buckets", [])}
    if not bucket_names:
        print("No available buckets found.")
        return None
    print("Existing buckets:")
    for name in bucket_names:
        print(f"- {name}")
    return None

def select_bucket(bucket_selected):
    """Prompts the user to select a valid S3 bucket and the list of buckets."""
    list_b = []
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    bucket_names = {bucket["Name"] for bucket in response.get("Buckets", [])}
    if not bucket_names:
        print("No available buckets found.")
        return None
    while True:
        if bucket_selected in bucket_names:
            return bucket_selected
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
        return False
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
        return False
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
def delete_object(bucket):
    """Deletes one object from """
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
    s3.delete_object(Bucket=bucket, key=selected_object)
    return

if __name__ == "__main__":
    CURRENT_BUCKET = None

    while True:
        menu_input = input(
            "Select 'q' to quit, 's' to select a bucket, 'u' to upload to a bucket, "
            "'lo' to list objects in a bucket, 'd' to download, 'psu' for a presigned "
            "url, 'del' to delete an object, 'l' to list the buckets: "
        ).strip().lower()

        match menu_input:
            case "q":
                break

            case "s":
                selection = input("Write the bucket you want selected: ")
                CURRENT_BUCKET = select_bucket(selection)
                if CURRENT_BUCKET:
                    print(f"Current bucket set to: {CURRENT_BUCKET}")

            case "u":
                if CURRENT_BUCKET is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    pathing = input("Enter the path to your file: ").strip()
                    name_of_file = input("Enter a name for the file or enter to skip: ").strip()
                    upload_file(pathing, CURRENT_BUCKET, name_of_file)

            case "lo":
                if CURRENT_BUCKET is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    object_list = list_objects(CURRENT_BUCKET)
                    print(object_list)

            case "d":
                if CURRENT_BUCKET is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    path_file = input("Enter the path to your file: ").strip()
                    download_file(CURRENT_BUCKET, path_file)

            case "psu":
                if CURRENT_BUCKET is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    url = pre_signed_url(CURRENT_BUCKET)
                    print(f"Your url is: {url}")

            case "v":
                if CURRENT_BUCKET is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    version_info = list_object_versions(CURRENT_BUCKET)
                    print(version_info)

            case "del":
                if CURRENT_BUCKET is None:
                    print("No bucket selected, please select a bucket.")
                else:
                    delete_object(CURRENT_BUCKET)

            case "l":
                bucket_listing()

            case _:
                print("Invalid option, please try again.")
