import requests
import json


class API:
    def __init__(self, header, url):
        self.headers = header
        self.url = url
        self.bot_id = 1

    def post_request(self, payload):
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.bot_id = int(r.json()["id"])
        return {"code": r.status_code, "json": r.json()}

    def get_request(self, bot_id):
        r = requests.get(f"{self.url}?bot_id={bot_id}", headers=self.headers)
        return {"code": r.status_code, "json": r.json()}

    def patch_request(self, bot_id, payload):
        r = requests.patch(f"{self.url}?bot_id={bot_id}", json=payload, headers=self.headers)
        return {"code": r.status_code, "json": r.json()}

    def put_request(self, bot_id, payload):
        r = requests.put(f"{self.url}?bot_id={bot_id}", json=payload, headers=self.headers)
        return {"code": r.status_code, "json": r.json()}

    def delete_request(self, bot_id):
        r = requests.delete(f"{self.url}?bot_id={bot_id}", headers=self.headers)
        return {"code": r.status_code}


