import json
import requests
from api_requests import API
import pytest

# execute with pytest -s --html=report.html

headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}
headers2 = {"Authorization": json.dumps({"username": "username2", "password": "password"})}


def test_post_invalid_data():
    r = requests.post("http://127.0.0.1:5000/", data="a", headers=headers)
    assert r.text == "Content-Type not supported!"
    assert r.status_code == 200


def test_post_no_data():
    r = requests.post("http://127.0.0.1:5000/", headers=headers)
    assert r.text == "Content-Type not supported!"  # or we could add another error for this one like "no payload provided"
    assert r.status_code == 200


def test_post_no_auth():
    j = {"url": "http://example.com"}
    r = requests.post("http://127.0.0.1:5000/", json=j)
    assert r.text == "No authorization credentials provided"
    assert r.status_code == 200


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
