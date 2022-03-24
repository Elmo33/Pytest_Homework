import json
import requests
from main import Main

headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}
headers2 = {"Authorization": json.dumps({"username": "username2", "password": "password"})}


# execute with pytest testing.py -s --html=report.html
def test_get_request():
    bot_id = 1
    r = requests.get(f"http://127.0.0.1:5000/?bot_id={bot_id}", headers=headers)

    assert json.dumps(r.json()) == json.dumps(Main.bots[bot_id])
    assert r.status_code == 200


def test_post_request():
    j = {"url": "http://example.com"}
    r = requests.post("http://127.0.0.1:5000/", json=j, headers=headers)
    assert r.status_code == 200


def test_put_request():
    j2 = {"intents": ["play-sound", "tell-joke"]}
    r = requests.put("http://127.0.0.1:5000/?bot_id=1", json=j2, headers=headers)

    assert r.status_code == 200


def test_patch_request():
    j3 = {"url": "http://example.com4362375"}
    r = requests.patch("http://127.0.0.1:5000/?bot_id=2", json=j3, headers=headers)
    assert r.status_code == 200


def test_delete_request():
    bot_id = 2
    r = requests.delete(f"http://127.0.0.1:5000/?bot_id={bot_id}", headers=headers)
    print(Main.bots)
    assert r.status_code == 200
# a = Flow("a")
