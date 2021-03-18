from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route('/fibonacci/<int:term>')
    def term(term):
        fib =[0,1]
        result = 0
        while result < term:
            result = fib[-1] + fib [-2]
            if (result < term):
                fib.append(result)
    return f"Output is: {fib}."


@app.route('/slack_alert/'<str:message>)
    def info(message):
        wekbook_url = 'https://hooks.slack.com/services/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'

        data = {
            'text': f'{message}.',
            'username': 'Test-bot',
            'icon_emoji': ':ghost:'
        }

        response = requests.post(wekbook_url, data=json.dumps(
            data), headers={'Content-Type': 'application/json'})

        print('Response: ' + str(response.text))
        print('Response code: ' + str(response.status_code))
        return jsonify()


@app.route('/is-prime/<int:n>')
def prime_check(n):
    return

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)