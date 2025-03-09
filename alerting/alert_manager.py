# FILE: /OpenAIOps/OpenAIOps/alerting/alert_manager.py

import requests
import json

class AlertManager:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_alert(self, message, alert_type="info"):
        payload = {
            "text": f"{alert_type.upper()}: {message}"
        }
        response = requests.post(self.webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        
        if response.status_code != 200:
            raise ValueError(f"Request to {self.webhook_url} returned an error {response.status_code}, the response is:\n{response.text}")

    def alert_on_condition(self, condition, message):
        if condition:
            self.send_alert(message, alert_type="warning")

    def alert_on_error(self, error_message):
        self.send_alert(error_message, alert_type="error")