import json
import pytest
from api_requests import API

# execute with pytest -s --html=report.html


headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}
headers2 = {"Authorization": json.dumps({"username": "username", "password": "password"})}
headers3 = {"Authorization": json.dumps({"token": "wrong"})}
headers4 = {"Authorization": json.dumps({"username": "username2", "password": "passw2ord"})}

first = API("http://127.0.0.1:5000/", headers)
second = API("http://127.0.0.1:5000/", headers2)
third = API("http://127.0.0.1:5000/", headers3)
fourth = API("http://127.0.0.1:5000/", headers4)

payload1 = {"url": "http://example.com"}
payload2 = {"url": "http://example.com4362375"}
payload3 = {"intents": ["play-sound", "tell-joke"]}


# @pytest.fixture()
# def demo_message():
#     print("Creating a new bot for this test case")
#     first.post_request(payload1)
#     print(f"New bot id is {first.bot_id}")
#     yield
#     print("Ending the test case")
#
#
# def test_get_request(demo_message):
#     result = first.get_request({"bot_id": first.bot_id})
#     assert result["status_code"] == 200


# THIS FUNCTION IS SO COOL, feel like a primate now for writing test cases separately
@pytest.mark.parametrize(
    ('input_x', 'code', 'expected'),
    (
            pytest.param(first.get_request({"bot_id": first.bot_id}), 200, None, id="First get request"),
            pytest.param(first.post_request(payload1), 200, {'id': first.bot_id, 'intents': [], 'name': 'test', 'url': 'http://example.com'},
                         id="First post request"),
            pytest.param(first.patch_request(first.bot_id, payload2), 200, None, id="First patch request"),
            pytest.param(first.put_request(first.bot_id, payload3), 200, None, id="First put request"),
            pytest.param(first.delete_request(first.bot_id), 200, None, id="First delete request"),
            pytest.param(second.get_request({"bot_id": first.bot_id}), 200, None, id="Second get request"),
            pytest.param(second.post_request(payload1), 200, {'id': first.bot_id, 'intents': [], 'name': 'test', 'url': 'http://example.com'},
                         id="Second post request"),
            pytest.param(second.patch_request(first.bot_id, payload2), 200, None, id="Second patch request"),
            pytest.param(second.put_request(first.bot_id, payload3), 200, None, id="Second put request"),
            pytest.param(second.delete_request(first.bot_id), 200, None, id="Second delete request"),

            pytest.param(first.post_request("a"), 200, {'error': 'Content-Type not supported!'}, id="Post with invalid data"),
            pytest.param(first.post_request(), 200, {'error': 'Content-Type not supported!'}, id="Post with no data"),
            pytest.param(third.post_request(payload1), 200, {"error": "wrong token code"}, id="Post with wrong secret"),
            pytest.param(fourth.post_request(payload1), 200, {"error": "wrong credentials"}, id="Post with wrong credentials"),
    )
)
def test_requests(input_x: dict, code, expected):
    result = input_x
    if expected:
        assert result["json"] == expected
    assert result["status_code"] == code
