import requests
import json

headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}


class API:
    def __init__(self, header, url):
        self.headers = header
        self.url = url
        self.bot_id = 1

    def post_request(self, payload, expected_code, expected_result=0, fixture=0):
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.bot_id = int(r.json()["id"])
        return r.status_code, r.json()

    def get_request(self, bot_id, expected_code, expected_result=0, fixture=0):
        r = requests.get(f"{self.url}?bot_id={bot_id}", headers=self.headers)
        return r.status_code, r.json()


ja = {"url": "http://example.com"}
first = API(headers, "http://127.0.0.1:5000/")


def test_post_request():
    result = first.post_request(ja, 200)
    assert result[0] == 200
    assert result[1] == {'id': first.bot_id, 'intents': [], 'name': 'test', 'url': 'http://example.com'}


def test_get_request():
    result = first.get_request(first.bot_id, 200)
    assert result[0] == 200

# first.get_request(first.bot_id, 200)
