import json
import pytest
from api_requests import API

headers = {"Authorization": json.dumps({"token": "sup3rs3cr3t"})}
first = API("http://127.0.0.1:5000/", headers)


def get_request(intent, answer, step_id):
    print({"intent": intent, "step": step_id, "answer": answer})
    result = first.get_request({"intent": intent, "step": step_id, "answer": answer})

    print(result["json"])
    print()
    return int(result["json"]["next"])


inte = 0
answ = 0
step = 0
steps_with_no_input_required = [0, 500, 555, 4]

# this is like a frontend part of the platform for interacting with the server
while True:
    step = get_request(inte, answ, step)
    if step not in steps_with_no_input_required:
        answ = input("enter: ")
    if step == 5:
        inte = answ
        answ = 0
        step = 0
    if step == 4 or step == 555:
        inte = 0
        answ = 0
        step = 0
    if step == 500:
        break
