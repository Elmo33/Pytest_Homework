# flatrock

"EVERY time the bot attempts to execute a command for example: play_sound it should check in the current configuration if the bot supports it."

^ this part of the task wasn't clear, and I think it's the only thing that's lacking from my code.

Also, as I haven't really worked much with pytest nor touched a good code written for it, my test cases may be little lacking, but of course that's fixable.

api_requests.py - class for requests

main.py - for launching the server via flask

test_positive_cases.py - positive test cases 

test_negative_cases.py - negative test cases 

report.html - generated pytest report


### first run the server and then test cases by using 
```
pytest -s --html=report.html
```

