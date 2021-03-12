"""
unit_tests.py
====================================
The file includes unit tests.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import *
from requests.auth import HTTPBasicAuth
import json

client = TestClient(app)

noauth = HTTPBasicAuth(username="u", password="p")
okauth = HTTPBasicAuth(username="user", password="pass")

def test_generate_keys_noauth():
    """
    Failed authorization test in the /generate_keys method.
    """
    response = client.get("/generate_keys", auth=noauth)
    assert response.status_code == 401

def test_encode_noauth():
    """
    Failed authorization test in the /encode method.
    """
    json={"original_text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor...",
    "public_key": ["0x251ada32935bee7de70a4b5", "0x677633cd88ea703ca9bc69b"]}
    response = client.post("/encode", auth=noauth, json=json)
    assert response.status_code == 401

def test_decode_noauth():
    """
    Failed authorization test in the /decode method.
    """
    auth = HTTPBasicAuth(username="u", password="p")
    json={"encode_text": ["0x2203322bf36c00d38e4b4ee","0x5d0961d520dd44f457cb297","0x4ca3cf515a7890b75b9e1b6",
    "0x46cebbdd97bd429bca42e4","0x636c82a6fa685d25a873f5","0x2acf8a4c29dc645784cf9da","0x1b9993999f0625a677d963b",
    "0x2f247f4fb1cf706b5dfff6d","0x4b631723c890bc91b76a7b0","0x5a7fcf9ae0bb58fd326d2ea","0x636c82a6fa685d25a873f5",
    "0x2acf8a4c29dc645784cf9da","0x35288586ca9cfc50d8b8d9f","0x5d0961d520dd44f457cb297","0x1950d271b14f68992f2c95d",
    "0x5d0961d520dd44f457cb297","0x4ca3cf515a7890b75b9e1b6","0x2acf8a4c29dc645784cf9da","0x4b631723c890bc91b76a7b0",
    "0x1b9993999f0625a677d963b","0xe1ca4850a4b869a1509e47","0x2acf8a4c29dc645784cf9da","0x4cf4a2d2de8926b14dd2f03",
    "0x636c82a6fa685d25a873f5","0x46cebbdd97bd429bca42e4","0xe1ca4850a4b869a1509e47","0x6176ba8fc67976bcb43e89b",
    "0x2acf8a4c29dc645784cf9da","0x56b730a0f2b20c16feb0d29","0x5d0961d520dd44f457cb297","0x57ed6b0ce16bdebe98798bb",
    "0x4b631723c890bc91b76a7b0","0x46cebbdd97bd429bca42e4","0x56b730a0f2b20c16feb0d29","0xe1ca4850a4b869a1509e47",
    "0x46cebbdd97bd429bca42e4","0xe1ca4850a4b869a1509e47","0x5a7fcf9ae0bb58fd326d2ea","0x4ca3cf515a7890b75b9e1b6",
    "0x2acf8a4c29dc645784cf9da","0x4cf4a2d2de8926b14dd2f03","0x35288586ca9cfc50d8b8d9f","0x1b9993999f0625a677d963b",
    "0x2f247f4fb1cf706b5dfff6d","0x1b9993999f0625a677d963b","0x4b631723c890bc91b76a7b0","0x56b730a0f2b20c16feb0d29",
    "0x1b9993999f0625a677d963b","0x57ed6b0ce16bdebe98798bb","0x72921a61d8e5a3f9336a2c","0x2acf8a4c29dc645784cf9da",
    "0x46cebbdd97bd429bca42e4","0x1950d271b14f68992f2c95d","0x1b9993999f0625a677d963b","0xe1ca4850a4b869a1509e47",
    "0x6176ba8fc67976bcb43e89b","0x2acf8a4c29dc645784cf9da","0x4b631723c890bc91b76a7b0","0x46cebbdd97bd429bca42e4",
    "0x35288586ca9cfc50d8b8d9f","0x2acf8a4c29dc645784cf9da","0x35288586ca9cfc50d8b8d9f","0x5d0961d520dd44f457cb297",
    "0x2acf8a4c29dc645784cf9da","0x46cebbdd97bd429bca42e4","0x1b9993999f0625a677d963b","0x5a7fcf9ae0bb58fd326d2ea",
    "0x4b631723c890bc91b76a7b0","0x636c82a6fa685d25a873f5","0x5d0961d520dd44f457cb297","0x35288586ca9cfc50d8b8d9f",
    "0x2acf8a4c29dc645784cf9da","0xe1ca4850a4b869a1509e47","0x46cebbdd97bd429bca42e4","0x636c82a6fa685d25a873f5",
    "0x2f247f4fb1cf706b5dfff6d","0x5d0961d520dd44f457cb297","0x4ca3cf515a7890b75b9e1b6","0x10656d4209725e74c282aca",
    "0x10656d4209725e74c282aca","0x10656d4209725e74c282aca"], 
    "private_key": ["0x5d4d90f7e5c087b2730e7dd", "0x677633cd88ea703ca9bc69b"]}
    response = client.post("/decode", auth=noauth, json=json)
    assert response.status_code == 401

def test_code_decode_auth():
    """
    Text encoding and decoding test and successful authorization test for all methods.
    """
    response = client.get("/generate_keys", auth=okauth)
    json_data = json.loads(response.text)
    public_key = json_data["public_key"]
    private_key = json_data["private_key"]
    
    original_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor..."
    json_to_send={"original_text": original_text, "public_key": public_key}
    response = client.post("/encode", auth=okauth, json=json_to_send)
    json_data = json.loads(response.text)
    encode_text = json_data["encode_text"]
    
    json_to_send={"encode_text": encode_text, "private_key": private_key}
    response = client.post("/decode", auth=okauth, json=json_to_send)
    json_data = json.loads(response.text)
    original_text_processed = json_data["original_text"]
    
    if original_text != original_text_processed:
        print("The processed text is different from the original.")
        
test_generate_keys_noauth()
test_encode_noauth()
test_decode_noauth()
test_code_decode_auth()
