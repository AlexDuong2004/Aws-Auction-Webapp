"""Tests the buckets, and objects within it"""
import os
from main import upload_file, list_objects, delete_object, bucket_listing

def test_listing_buckets():
    """Displays the current buckets, demo1452 was made as an example"""
    current_buckets = {'demo1452', 'hw03-ald21039-2', 'hw03-ald21039-1', 'hw03-ald21039-3'}
    assert bucket_listing() == current_buckets

def test_list_bucket_contents():
    """Displays the contents of the selected bucket, made for githubactions pytest"""
    assert list_objects('hw03-ald21039-2') == []
    assert list_objects('hw03-ald21039-3') == []
    assert list_objects('hw03-ald21039-1') == []

def test_upload_object():
    """Tests to see if files are uploaded correctly"""
    repo_root = os.getcwd()
    file_path1 = os.path.join(repo_root, "hw03", "pytest_files", "dummyfile1.txt")
    file_path2 = os.path.join(repo_root, "hw03", "pytest_files", "dummyfile2.txt")
    upload_file(file_path1,'hw03-ald21039-1')
    assert list_objects('hw03-ald21039-1') == ['dummyfile1.txt']
    upload_file(file_path2,'hw03-ald21039-1')
    assert list_objects('hw03-ald21039-1') == ['dummyfile1.txt', 'dummyfile2.txt']
    upload_file(file_path2, 'hw03-ald21039-2')
    assert list_objects('hw03-ald21039-2') == ['dummyfile2.txt']

def test_delete_object():
    """Tests to see if objects are deleted properly"""
    repo_root = os.getcwd()
    file_path1 = os.path.join(repo_root, "hw03", "pytest_files", "dummyfile1.txt")
    file_path2 = os.path.join(repo_root, "hw03", "pytest_files", "dummyfile2.txt")
    delete_object('hw03-ald21039-1', 'dummyfile2.txt')
    assert list_objects('hw03-ald21039-1') == ['dummyfile1.txt']
    delete_object('hw03-ald21039-1', 'dummyfile1.txt')
    assert list_objects('hw03-ald21039-1') == []
    delete_object('hw03-ald21039-1', 'dummyfile2.txt')
    assert list_objects('hw03-ald21039-1') == []
