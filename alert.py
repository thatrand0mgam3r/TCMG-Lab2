import requests
import json

# from flask import Flask
# app = Flask(__name__)

# @app.route('/slack_alert/<string:mes>')

def slack_alert(msg):
    data = {'text':msg}
    resp = requests.post(SLACK_URL, json=data)
    if resp.status_code == 200:
        result = True
        mesg = "Post Accepted"
    else: # gives the error and message should the message result in a failure
        result= False
        mesg: "Please try again (HTTP error: "str(response.status_code)")
        
    return jsonify(#attempts to json the data and give the response code for error.
        input=msg,
        message=mesg,
        output=result
    ),200 if resp.status_code==200 else 400


