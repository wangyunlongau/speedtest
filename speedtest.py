import subprocess
import http.client
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

result = subprocess.run('/usr/local/bin/speedtest',
                        stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()

lines = []
for line in result:
    line = line.strip().replace(',', '')
    line = ' '.join(line.split())
    if line:
        lines.append(line)

slack_msg = '\n'.join(lines)

payload = {"text": slack_msg}

connection = http.client.HTTPSConnection('hooks.slack.com')
connection.request(
    'POST', 'INCOMING_WEBHOOK_PATH', json.dumps(payload))
response = connection.getresponse()
