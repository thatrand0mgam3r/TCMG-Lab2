from flask import Flask, Response, jsonify

app = Flask(__name__)

@app.route("/factorial/<int:n>")
def factorial(n):
    if n == 1:
        return f"input: {n}"
    else:
        return {n} + 2 
    


@app.route('/json')
def json_response():
    #resp = Response('{ "foo": "bar", "baz": "bat" }')
    #resp.headers ['Content-Type'] = 'application/json'
    #return resp
    return jsonify(foo='bar', bar='baz' )



