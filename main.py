from flask import Flask, request
import json
from bot import Bot

app = Flask(__name__)


class Main:

    def __init__(self):
        self.__username = "username"
        self.__password = "password"
        self.__token = "sup3rs3cr3t"
        self.content_type = ""

    def check_auth(self):  # checking if there is a token or username/password in the header
        auth = json.loads(request.headers["Authorization"])
        if "token" in auth.keys() and auth["token"] != self.__token:
            return {"error": "wrong token code"}
        elif "username" in auth.keys() and (auth["username"] != self.__username or auth["password"] != self.__password):
            return {"error": "wrong credentials"}
        else:
            return 0

    def check_type(self):
        if self.content_type != 'application/json':
            return {"error": 'Content-Type not supported!'}

    @staticmethod
    def post_request():
        json_load = request.json
        new_bot = Bot(json_load["url"])
        new_bot.add_to_db()
        return Bot.bots[new_bot.id]

    @staticmethod
    def get_request():
        args = request.args
        print(args)
        if "intent" not in args:
            if "bot_id" not in args:
                return Bot.bots
            elif int(args.get("bot_id")) not in Bot.bots.keys():
                return {"error": "No such bot found"}
            else:
                return Bot.bots[int(args.get("bot_id"))]
        else:
            if request.args["intent"] == "0":
                return {"text": "What do you want bot to do? \n1)Tell a joke\n2)Play_sound\n3)DisconnecT", "next": 5}
            elif request.args["intent"] == "1":
                if "step" in request.args:
                    return Bot.tell_a_joke({"id": int(request.args["step"]), "answer": request.args["answer"]})
                else:
                    return Bot.tell_a_joke({"id": 0})
            elif request.args["intent"] == "2":
                if "step" in request.args:
                    return Bot.play_sound({"id": int(request.args["step"]), "answer": request.args["answer"]})
                else:
                    return Bot.play_sound({"id": 0})
            elif request.args["intent"] == "3":
                return Bot.disconnect()
            else:
                return {"text": "wrong number dude", "next": 555}

    @staticmethod
    def delete_request():
        args = request.args
        del Bot.bots[int(args.get("bot_id"))]
        return "bot successfully deleted"

    @staticmethod
    def put_request():
        json_load = request.json
        bot_id = int(request.args.get("bot_id"))
        Bot.bots[bot_id] = {"id": bot_id, "intents": json_load["intents"], "name": "test"}
        return Bot.bots[bot_id]

    @staticmethod
    def patch_request():
        json_load = request.json
        bot_id = int(request.args.get("bot_id"))
        Bot.bots[bot_id]["url"] = json_load["url"]
        return Bot.bots[bot_id]

    def respond(self):
        self.content_type = request.headers.get('Content-Type')

        if "Authorization" not in request.headers:
            return {"error": "No authorization credentials provided"}

        not_validated = self.check_auth()
        if not_validated:
            return not_validated

        load_type = self.check_type()
        if request.method in ["POST", "PUT", "PATCH"] and load_type is not None:
            return load_type

        # ---------------------------- POST ---------------------------------#
        if request.method == 'POST':
            return self.post_request()
        # ---------------------------- GET ----------------------------------#
        elif request.method == 'GET':
            return self.get_request()
        # ---------------------------- DELETE -------------------------------#
        elif request.method == 'DELETE':
            return self.delete_request()
        # ---------------------------- PUT ----------------------------------#
        elif request.method == 'PUT':
            return self.put_request()
        # ---------------------------- PATCH -------------------------------#
        elif request.method == 'PATCH':
            return self.patch_request()


@app.route('/', methods=['POST', 'GET', 'DELETE', 'PUT', 'PATCH'])
def home():
    return Main().respond()


if __name__ == '__main__':
    app.run(debug=True)
