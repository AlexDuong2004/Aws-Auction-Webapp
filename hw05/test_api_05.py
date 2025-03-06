import requests
import os
from requests_toolbelt import MultipartEncoder


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

def test_upload_and_delete():
    """Uploads an object to a selected bucket and properly deletes it and makes sure of it"""
    repo_root = os.getcwd()
    file_path1 = os.path.join(repo_root, "hw05", "pytest_files", "dummy1.txt")
    url_2 = "https://rws5qyu8l9.execute-api.us-east-1.amazonaws.com/dev/hw05-ald21039-1"
    response_2 = requests.get(url_2)
    assert response_2.status_code == 200
    assert response_2.json().get("Objects", []) == []
    object_name = "dummy1"
    
    with open(file_path1, 'rb') as file:
        file_data = file.read()

    m = MultipartEncoder(
        fields={
            'file': (object_name, file_data, 'text/plain'),  
            'object_name': object_name                      
        }
    )

    response_3 = requests.post(url_2, data=m, headers={'Content-Type': m.content_type})

    assert response_3.status_code == 201
    uploaded_object = response_3.json().get("file_name")
    assert uploaded_object == object_name
    response_4 = requests.get(url_2)
    assert response_4.status_code == 200
    assert response_4.json().get("Objects", []) == ["dummy1"]
    url_5 = "https://rws5qyu8l9.execute-api.us-east-1.amazonaws.com/dev/hw05-ald21039-1/dummyfile1"
    response_5 = requests.delete(url_5)
    assert response_5.status_code == 200
    response_6 = requests.get(url_2)
    assert response_6.status_code == 200
    assert response_6.json().get("Objects", []) == []




