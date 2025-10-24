import requests

def monitor_server_health(server_url, slack_webhook):
    try:
        response = requests.get(server_url)

        if response.status_code == 200:
            message = f"server {server_url}is UP!"
        else:
            message = f"server {server_url}is Down! status code:{response.status_code}"

        #send notification to slack
        slack_data = {'text': message}
        slack_response = requests.post(slack_webhook, json=slack_data)

        if slack_response.status_code == 200:
            print(f"slack notification sent: {message}")
        else:
            print(f"failed to send slack notification.Status Code:{slack_response.status_code}")
   
    except requests.exceptions.RequestException as e:
        print(f"Error while checking server health: {e}")
        error_message = f"error while checking server health: {e}"
        requests.post(slack_webhook, json={'text': error_message})

#example
server_url =  "https://example.com"
slack_webhook = "https://hooks.slack.com/services/your/webhook/url"
monitor_server_health(server_url, slack_webhook)