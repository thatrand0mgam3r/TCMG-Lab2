import requests
import json

if __name__ == '__main__':

    wekbook_url = 'https://hooks.slack.com/services/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'

    data = {
        'text': ' Testing comms.',
        'username': 'Test-bot',
        'icon_emoji': ':ghost:'
    }

    response = requests.post(wekbook_url, data=json.dumps(
        data), headers={'Content-Type': 'application/json'})

    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))

