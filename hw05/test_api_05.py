import requests
import boto3


def test_list_buckets():
    """Looks to see if it listed every single bucket"""
    current_buckets = ["demo1452", "hw03-ald21039-1", "hw03-ald21039-2", "hw03-ald21039-3", "hw04-ald21039-1", "hw05-ald21039-1", "hw05-ald21039-2", "hw05-ald21039-3"]
    url =  "https://rws5qyu8l9.execute-api.us-east-1.amazonaws.com/dev/list"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json().get("buckets", []) == current_buckets
    assert len(response.json().get("buckets", [])) == 8
    
def test_list_objects():
    """Looks to see the objects in the selected bucket"""
    url_1 = "https://rws5qyu8l9.execute-api.us-east-1.amazonaws.com/dev/hw04-ald21039-1"
    hw04_bucket = ["dummy.jpg", "dummyfile1.txt", "dummyfile2.txt"]
    response_1 = requests.get(url_1)
    assert response_1.status_code == 200
    assert response_1.json().get("Objects", []) == hw04_bucket
    url_2 = "https://rws5qyu8l9.execute-api.us-east-1.amazonaws.com/dev/hw05-ald21039-1"
    response_2 = requests.get(url_2)
    assert response_2.status_code == 200
    assert response_2.json().get("Objects", []) == []
    url_3 = "https://rws5qyu8l9.execute-api.us-east-1.amazonaws.com/dev/hw05-ald21039-2"
    response_3 = requests.get(url_3)
    assert response_3.status_code == 200
    assert response_3.json().get("Objects", []) == []
    url_4 = "https://rws5qyu8l9.execute-api.us-east-1.amazonaws.com/dev/hw05-ald21039-3"
    response_4 = requests.get(url_4)
    assert response_4.status_code == 200
    assert response_4.json().get("Objects", []) == []

