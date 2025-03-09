# FILE: /OpenAIOps/OpenAIOps/alerting/alert_rules.py
class AlertRule:
    def __init__(self, name, condition, severity):
        self.name = name
        self.condition = condition
        self.severity = severity

    def evaluate(self, data):
        # Evaluate the condition against the provided data
        return eval(self.condition)

# Example alert rules
alert_rules = [
    AlertRule("High CPU Usage", "data['cpu_usage'] > 80", "critical"),
    AlertRule("Memory Leak", "data['memory_usage'] > data['memory_limit'] * 0.9", "warning"),
    AlertRule("Disk Space Low", "data['disk_space'] < 10", "critical"),
]

def check_alerts(data):
    triggered_alerts = []
    for rule in alert_rules:
        if rule.evaluate(data):
            triggered_alerts.append(rule)
    return triggered_alerts