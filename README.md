# speedtest
Test network speed using Speedtest by Ookla. The result is published to Slack. The tool can be used to monitor if network speed doesn't meet SLA with ISP.

Setup:
- install [speedtest cli](https://www.speedtest.net/apps/cli)
- create an [incoming webhook](https://api.slack.com/messaging/webhooks) to post speed test result into Slack

Run test:
```bash
python3 speedtest.py
```

Run test as cron job:
```bash
0 19 * * * cd /path/speedtest && /path/3.8/bin/python3 speedtest.py
```
