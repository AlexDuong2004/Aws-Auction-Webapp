import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image
import base64
            
s3_client = boto3.client('s3')
            
def resize_image(image_path, resized_path):
  """Halves the thumnail size"""
  with Image.open(image_path) as image:
    image.thumbnail(tuple(x / 2 for x in image.size))
    image.save(resized_path)
    with open(resized_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
        print(f"Base64 Thumbnail Preview: {encoded_string[:200]}... (truncated)")
            
def thumbnail_generator(event, context):
  for record in event['Records']:
    bucket = record['s3']['bucket']['name']
    key = unquote_plus(record['s3']['object']['key'])
    tmpkey = key.replace('/', '')
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
    upload_path = '/tmp/resized-{}'.format(tmpkey)
    s3_client.download_file(bucket, key, download_path)
    resize_image(download_path, upload_path)
    s3_client.upload_file(upload_path, '{}-resized'.format(bucket), 'resized-{}'.format(key))