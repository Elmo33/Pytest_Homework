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
    first.headers = headers  # setting headers back to their value
    assert result.text == "No authorization credentials provided"
    assert result.status_code == 200


def test_post_wrong_token():
    wrong = {"Authorization": json.dumps({"token": "wrong"})}
    j = {"url": "http://example.com"}
    r = requests.post("http://127.0.0.1:5000/", json=j, headers=wrong)
    assert r.text == "wrong token code"
    assert r.status_code == 200


def test_post_wrong_credentials():
    wrong = {"Authorization": json.dumps({"username": "username2", "password": "passw2ord"})}
    j = {"url": "http://example.com"}
    r = requests.post("http://127.0.0.1:5000/", json=j, headers=wrong)
    assert r.text == "wrong credentials"
    assert r.status_code == 200
