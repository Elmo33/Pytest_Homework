# flatrock

### Server 
bot.py - class for bots

server.py - for launching the server via flask

### Testing
api_requests.py - class for requests

interact.py - "interface" for interacting with intents. for manual testing.

test_cases.py - all test cases

test_intents.py - fully automated testing of tell_joke

### assets
style.css - for styling the html report

report.html - generated pytest report
### first run the server and then test cases by using 
```
pytest -sv --html=report.html
```

Required libraries: json, pytest, pytest-html, flask, requests
