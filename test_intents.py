import json
from api_requests import API
import pytest


class Interaction:
    def __init__(self, intent=0, answer=0, step=0):
        self.intent = intent
        self.answer = answer
        self.step = step

    def reset(self):
        self.intent, self.answer, self.step = 0, 0, 0

    def payload(self):
        a = {"intent": self.intent, "step": self.step, "answer": self.answer}
        self.reset()
        return a


@pytest.fixture
def tester(intent, answer, step):
    return Interaction(intent, answer, step)


headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}
first = API("http://127.0.0.1:5000/", headers)


@pytest.mark.parametrize(('intent', 'step', 'answer', 'expected'),
                         ((0, 0, 0, {'next': 5, 'text': 'What do you want bot to do? \n1)Tell a joke\n2)Play_sound\n3)DisconnecT'}),
                          (555, 0, 0, {'next': 555, 'text': 'wrong number dude'}),
                          (1, 0, 0, {'next': 1, 'text': 'Which bot do you want to tell a joke? (id)'}),
                          (1, 1, 555, {'next': 0, 'text': 'Sorry there is no such bot'}),
                          (1, 1, 2, {'next': 0, 'text': 'Sorry this Bot has no sense of humour :(('}),
                          (1, 1, 1, {'next': 2, 'text': 'Knock, Knock'}),
                          (1, 2, 'what', {'next': 2, 'text': 'Common you know what to answer, KNOCK, KNOCK!'}),
                          (1, 2, 'who is it', {'next': 3, 'text': 'Nobel'}),
                          (1, 3, 'what', {'next': 3, 'text': "that's not what you are supposed to answer -_-, lets try again, its Nobel"}),
                          (1, 3, 'nobel who', {'next': 4, 'text': "Nobel...that's why I knocked"}),
                          ))
def test_tell_joke(tester, intent, answer, step, expected):
    request = first.get_request(tester.payload())
    assert request["json"] == expected
