# flatrock

only with this task I discovered a lot of pytest functionalities
that changes a lot about how I'll be using it, and only learned all of this in 2 days, so I need more real opportunities to learn the rest.

api_requests.py - class for requests

bot.py - class for bots

interact.py - "interface" for interacting with intents. for manual testing.

main.py - for launching the server via flask

test_cases.py - positive test cases 

report.html - generated pytest report

test_intents.py - fully automated testing of tell_joke
### first run the server and then test cases by using 
```
pytest -s --html=report.html
```

Required libraries: json, pytest, pytest-html, flask, requests
