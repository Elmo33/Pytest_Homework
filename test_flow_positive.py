import json
import requests
import pytest

# execute with pytest -s --html=report.html

headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}
headers2 = {"Authorization": json.dumps({"username": "username2", "password": "password"})}


@pytest.fixture()
def demo_message():
    print("\nStarting to launch the test case")
    print("----------------------------------")
    yield
    print("Ending the test case")


bot_id = 0


def test_post_request():
    j = {"url": "http://example.com"}
    r = requests.post("http://127.0.0.1:5000/", json=j, headers=headers)
    global bot_id
    bot_id = int(r.json()["id"])
    assert r.status_code == 200


def test_get_request(demo_message):
    r = requests.get(f"http://127.0.0.1:5000/?bot_id={bot_id}", headers=headers)
    assert r.status_code == 200


def test_get_request_no_specify():
    r = requests.get(f"http://127.0.0.1:5000/", headers=headers)
    assert r.status_code == 200


def test_patch_request():
    j3 = {"url": "http://example.com4362375"}
    r = requests.patch(f"http://127.0.0.1:5000/?bot_id={bot_id}", json=j3, headers=headers)
    assert r.status_code == 200


def test_put_request():
    j2 = {"intents": ["play-sound", "tell-joke"]}
    r = requests.put(f"http://127.0.0.1:5000/?bot_id={bot_id}", json=j2, headers=headers)
    assert r.status_code == 200


def test_delete_request():
    r = requests.delete(f"http://127.0.0.1:5000/?bot_id={bot_id}", headers=headers)
    assert r.status_code == 200


@pytest.mark.skipif(2 == 2, reason="just for demo")
def test_just_skip():
    assert 2 == 1

@pytest.mark.xfail
def test_just_fail():
    test_just_skip()
