
# Playwright simple automation task

1. Open https://dialer018.talkasiavoip.cc/
2. Click Agent Login
3. Take User / Pass from a text File that contains following
    USER ID: 8000
    PASS: 123qwe123
4. Click Submit
5. Login again with same details. 
6. Choose campaign ID, if campaign ID gives you an error, Print Error in Console and Submit the task. 

## Installation
```
    pip install -r requirements.txt
    playwright install
```
playwright Installation make take up to 10min.

## Run
```
    python task.py
```
The task will go throw the steps montined above. and you will find all the outputs on options.json