from flask import Flask, request
import json

app = Flask(__name__)


class Main:
    bots = {1: {"id": 1, "intents": ["play_sound", "tell_joke", "disconnect"], "name": "first", "url": "example.com"},
            2: {"id": 2, "intents": ["play_sound", "tell_joke"], "name": "second", "url": "example2.com"}}

    def __init__(self):
        self.__username = "username"
        self.__password = "password"
        self.__token = "sup3rs3cr3t"

    def check_auth(self):  # checking if there is a token or username/password in the header
        auth = json.loads(request.headers["Authorization"])
        if "token" in auth.keys() and auth["token"] != self.__token:
            return "wrong token code"
        elif "username" in auth.keys() and (auth["username"] != self.__username or auth["password"] != self.__password):
            return "wrong credentials"
        else:
            return 0

    def respond(self):
        content_type = request.headers.get('Content-Type')

        not_validated = self.check_auth()
        if not_validated:
            return not_validated

        # ---------------------------- POST ---------------------------------#
        if request.method == 'POST':
            if content_type == 'application/json':
                json_load = request.json
                new_id = max(self.bots.keys()) + 1
                self.bots[new_id] = {"id": new_id, "name": "test", "intents": [], "url": json_load["url"]}
                return self.bots[new_id]
            else:
                return 'Content-Type not supported!'

        # ---------------------------- GET ----------------------------------#
        if request.method == 'GET':
            args = request.args
            return self.bots[int(args.get("bot_id"))]

        # ---------------------------- DELETE -------------------------------#
        if request.method == 'DELETE':
            args = request.args
            del self.bots[int(args.get("bot_id"))]
            return "bot successfully deleted"

        # ---------------------------- PUT ----------------------------------#
        if request.method == 'PUT':
            if content_type == 'application/json':
                json_load = request.json
                bot_id = int(request.args.get("bot_id"))
                self.bots[bot_id] = {"id": bot_id, "intents": json_load["intents"], "name": "test"}
                return self.bots[bot_id]
            else:
                return 'Content-Type not supported!'

        # ---------------------------- PATCH -------------------------------#
        if request.method == 'PATCH':
            if content_type == 'application/json':
                json_load = request.json
                bot_id = int(request.args.get("bot_id"))
                self.bots[bot_id]["url"] = json_load["url"]
                return self.bots[bot_id]
            else:
                return 'Content-Type not supported!'


@app.route('/', methods=['POST', 'GET', 'DELETE', 'PUT', 'PATCH'])
def home():
    return Main().respond()

if __name__ == '__main__':
    app.run(debug=True)
