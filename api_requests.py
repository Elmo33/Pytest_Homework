import requests


class API:
    def __init__(self, url, header=0):
        self.headers = header
        self.url = url
        self.bot_id = 1

    def post_request(self, payload):
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.bot_id = int(r.json()["id"])
        return r

    def get_request(self, bot_id):
        r = requests.get(f"{self.url}?bot_id={bot_id}", headers=self.headers)
        return r

    def patch_request(self, bot_id, payload):
        r = requests.patch(f"{self.url}?bot_id={bot_id}", json=payload, headers=self.headers)
        return r

    def put_request(self, bot_id, payload):
        r = requests.put(f"{self.url}?bot_id={bot_id}", json=payload, headers=self.headers)
        return r

    def delete_request(self, bot_id):
        r = requests.delete(f"{self.url}?bot_id={bot_id}", headers=self.headers)
        return r


