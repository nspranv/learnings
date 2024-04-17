from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def jira_webhook():
    data = request.json

    if 'issue' in data and data['issue']['key'] == 'YOUR_SPECIFIC_ISSUE_KEY':
        # Check if the issue was transitioned to "Done"
        if data['webhookEvent'] == 'jira:issue_updated' and 'transition' in data['issue']['fields']:
            transition = data['issue']['fields']['transition']
            if transition['to_status']['name'] == 'Done':
                execute_script()
                return 'Script executed successfully', 200

    return 'Issue not transitioned to "Done"', 200

def execute_script():
    # create slack channel

if __name__ == '__main__':
    app.run(debug=True)
