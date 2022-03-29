import requests


class API:
    def __init__(self, url, header):
        self.headers = header
        self.url = url
        self.bot_id = 1

    def post_request(self, payload=None):
        if payload is None:
            r = requests.post(self.url, headers=self.headers)
        elif type(payload) == str:
            r = requests.post(self.url, data=payload, headers=self.headers)
        else:
            r = requests.post(self.url, json=payload, headers=self.headers)
            if 'error' not in r.json():
                self.bot_id = int(r.json()["id"])
        return {"status_code": r.status_code, "json": r.json()}

    def get_request(self, reqs):
        attributes = "".join([f"{i}={reqs[i]}&" for i in reqs.keys()])[:-1]
        r = requests.get(f"{self.url}?{attributes}", headers=self.headers)
        return {"status_code": r.status_code, "json": r.json()}

    def patch_request(self, bot_id, payload):
        r = requests.patch(f"{self.url}?bot_id={bot_id}", json=payload, headers=self.headers)
        return {"status_code": r.status_code, "json": r.json()}

    def put_request(self, bot_id, payload):
        r = requests.put(f"{self.url}?bot_id={bot_id}", json=payload, headers=self.headers)
        return {"status_code": r.status_code, "json": r.json()}

    def delete_request(self, bot_id):
        r = requests.delete(f"{self.url}?bot_id={bot_id}", headers=self.headers)
        return {"status_code": r.status_code, "json": r.text}
