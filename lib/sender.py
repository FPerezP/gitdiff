import smtplib
from email.mime.text import MIMEText
import yaml
import logging

class Sender():
    def __init__(self, commitList):
        self.body = ''

        if not commitList:
            raise ValueError('Empty commit list')
        self.commitList = commitList
        self.body = self.format_email_body()

    def format_email_body(self):
        body = ''
        for commit in self.commitList:
            diff = commit.getDiff()
            if not diff:
                continue
            body += str(commit)
        return body

    def send(self, template):
        config = yaml.load(open('config.yaml'))
        smtp_config = config.get('smtp')

        message = MIMEText(template, 'html')
        message['Subject'] = smtp_config['subject']
        message['From'] = smtp_config['from']
        message['To'] = smtp_config['to']

        smtpserver = smtplib.SMTP(smtp_config['host'], int(smtp_config['port']))
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(smtp_config['login'], smtp_config['password'])

        smtpserver.sendmail(smtp_config['from'], smtp_config['to'], message.as_string())
        smtpserver.close()