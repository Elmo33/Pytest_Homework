import json
import requests
from api_requests import API
import pytest

# execute with pytest -s --html=report.html


headers2 = {"Authorization": json.dumps({"username": "username2", "password": "password"})}

headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}
first = API("http://127.0.0.1:5000/", headers)


def test_post_invalid_data():
    result = first.post_request("a")
    assert result.text == "Content-Type not supported!"
    assert result.status_code == 200


def test_post_no_data():
    result = first.post_request()
    assert result.text == "Content-Type not supported!"  # or we could add another error for this one like "no payload provided"
    assert result.status_code == 200


def test_post_no_auth():
    first.headers = None
    payload = {"url": "http://example.com"}
    result = first.post_request(payload)
    assert result.text == "No authorization credentials provided"
    assert result.status_code == 200

    first.headers = headers  # setting headers back to their value


def test_post_wrong_token():
    first.headers = {"Authorization": json.dumps({"token": "wrong"})}
    payload = {"url": "http://example.com"}
    result = first.post_request(payload)
    assert result.text == "wrong token code"
    assert result.status_code == 200

    first.headers = headers  # setting headers back to their value


def test_post_wrong_credentials():
    first.headers = {"Authorization": json.dumps({"username": "username2", "password": "passw2ord"})}
    payload = {"url": "http://example.com"}
    result = first.post_request(payload)
    assert result.text == "wrong credentials"
    assert result.status_code == 200

    first.headers = headers  # setting headers back to their value
