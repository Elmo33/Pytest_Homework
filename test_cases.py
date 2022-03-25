import json
import pytest
from api_requests import API


# execute with pytest -s --html=report.html

@pytest.fixture()
def demo_message():
    print("\nStarting to launch the test case")
    print("----------------------------------")
    yield
    print("Ending the test case")


# ------------------------------------------------------------ FIRST FLOW ------------------------------------------------------
headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}
first = API("http://127.0.0.1:5000/", headers)


def test_post_request():
    payload = {"url": "http://example.com"}
    result = first.post_request(payload)
    assert result.status_code == 200
    assert result.json() == {'id': first.bot_id, 'intents': [], 'name': 'test', 'url': 'http://example.com'}


def test_get_request(demo_message):
    result = first.get_request(first.bot_id)
    assert result.status_code == 200


def test_patch_request():
    payload = {"url": "http://example.com4362375"}
    result = first.patch_request(first.bot_id, payload)
    assert result.status_code == 200


def test_put_request():
    payload = {"intents": ["play-sound", "tell-joke"]}
    result = first.put_request(first.bot_id, payload)
    assert result.status_code == 200


def test_delete_request():
    result = first.delete_request(first.bot_id)
    assert result.status_code == 200


# ------------------------------------------------------------ SECOND FLOW ------------------------------------------------------
headers2 = {"Authorization": json.dumps({"username": "username", "password": "password"})}
second = API("http://127.0.0.1:5000/", headers2)


def test_post_request2():
    payload = {"url": "http://example.com"}
    result = second.post_request(payload)
    assert result.status_code == 200
    assert result.json() == {'id': second.bot_id, 'intents': [], 'name': 'test', 'url': 'http://example.com'}


def test_get_request2(demo_message):
    result = second.get_request(second.bot_id)
    assert result.status_code == 200


def test_patch_request2():
    payload = {"url": "http://example.com4362375"}
    result = second.patch_request(second.bot_id, payload)
    assert result.status_code == 200


def test_put_request2():
    payload = {"intents": ["play-sound", "tell-joke"]}
    result = second.put_request(second.bot_id, payload)
    assert result.status_code == 200


def test_delete_request2():
    result = second.delete_request(second.bot_id)
    assert result.status_code == 200


@pytest.mark.skipif(2 == 2, reason="just for demo")
def test_just_skip():
    assert 2 == 1


@pytest.mark.xfail
def test_just_fail():
    test_just_skip()
