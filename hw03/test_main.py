"""Tests the buckets, and objects within it"""
import logging
import os
import boto3
import unittest
from main import select_bucket, upload_file, list_objects, delete_object, bucket_listing

def test_listing_buckets():
    """Displays the current buckets, demo1452 was made as an example"""
    current_buckets = ['demo1452', 'hw03-ald21039-2', 'hw03-ald21039-1', 'hw03-ald21039-3']
    assert bucket_listing() == current_buckets
