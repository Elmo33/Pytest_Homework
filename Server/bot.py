class Bot:
    bots = {1: {"id": 1, "intents": ["play_sound", "tell_joke", "disconnect"], "name": "first", "url": "example.com"},
            2: {"id": 2, "intents": ["play_sound", "disconnect"], "name": "oto", "url": "example2.com"}}  # named after my friend

    def __init__(self, url, name="example", intents=None):
        self.url = url
        self.name = name
        self.intents = intents
        self.id = None

    def add_to_db(self):
        self.id = max(self.bots.keys()) + 1
        Bot.bots[self.id] = {"id": self.id, "name": "test", "intents": [], "url": self.url}

    @staticmethod
    def menu():
        return {"text": "What do you want bot to do? \n1)Tell a joke\n2)Play_sound\n3)DisconnecT", "next": 5}

    @staticmethod
    def tell_a_joke(step):
        if step["id"] == 0:
            return {"text": "Which bot do you want to tell a joke? (id)", "next": 1}
        if step["id"] == 1:
            if int(step["answer"]) not in Bot.bots.keys():
                return {"text": "Sorry there is no such bot", "next": 0}
            elif "tell_joke" not in Bot.bots[int(step["answer"])]["intents"]:
                return {"text": "Sorry this Bot has no sense of humour :((", "next": 0}
            else:
                return {"text": "Knock, Knock", "next": 2}
        if step["id"] == 2:
            if step["answer"].lower() != "who's there" and step["answer"].lower() != "who is it":
                return {"text": "Common you know what to answer, KNOCK, KNOCK!", "next": 2}
            else:
                return {"text": "Nobel", "next": 3}
        if step["id"] == 3:
            if step["answer"].lower() != "nobel who":
                return {"text": "that's not what you are supposed to answer -_-, lets try again, its Nobel", "next": 3}
            return {"text": "Nobel...that's why I knocked", "next": 4}

    @staticmethod
    def play_sound(step):
        if step["id"] == 0:
            return {"text": "which bot do you want to play sound? (id)", "next": 1}
        if step["id"] == 1:
            if int(step["answer"]) not in Bot.bots.keys():
                return {"text": "Sorry there is no such bot", "next": 0}
            elif "play_sound" not in Bot.bots[int(step["answer"])]["intents"]:
                return {"text": "Sorry this cant play anything", "next": 0}
            else:
                return {"text": "lets pretend the sound is playing rn", "next": 4}

    @staticmethod
    def disconnect():
        return {"text": "disconnecting", "next": 500}
