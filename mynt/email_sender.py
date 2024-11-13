from typing import Any


import smtplib
from email.mime.text import MIMEText
from os import getenv

class SingletonMetaclass(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        assert not (args or kwargs), 'Singleton should not accept arguments'

        if isinstance(cls._instance, cls):
            return cls._instance
        else:
            cls._instance = super(SingletonMetaclass, cls).__call__()
            return cls._instance


class EmailSender(metaclass=SingletonMetaclass):

    def __init__(self):
        print("starting email sending service.")

        self.sender = getenv("SERVICE_EMAIL")
        self.smtpObj = smtplib.SMTP('smtp.gmail.com')

        self.smtpObj.ehlo()

        self.smtpObj.starttls()

        self.smtpObj.login(self.sender, getenv("SERVICE_EMAIL_PASSWD"))

    def send_email(self, subject, text, to):
        cont = '''\
        <html>
            <head></head>
            <body>
            <p>{0}</p>
            </body>
        </html>
        '''.format(text)

        msgTo = ""
        for person in to: 
            msgTo += "{0} ".format(person)

        msg = MIMEText(cont, 'html')

        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = msgTo


        self.smtpObj.sendmail(self.sender, to, msg.as_string())
