#!/usr/bin/python
# -*- coding:utf8 -*-


import yagmail
from threading import Thread


class MailClient():
    """
    :param host
    :param port
    :param use_ssl
    :param user
    :param passwd
    """

    def __init__(self, **config):
        self.host = config['host']
        self.port = config['port']
        self.use_ssl = config.get('use_ssl', True)
        self.user = config['user']
        self.password = config['password']

        self.client = yagmail.SMTP(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port,
                                    smtp_ssl=self.use_ssl)

    def send(self, to=None, subject=None, contents=None):
        """
        发送邮件
            :param to [str]: []
            :param subject str:
            :param contents [str]:
        """
        self.client.send(to=to, subject=subject, contents=contents)

    def async_send(self, to=None, subject="subject", contents=None):
        """
        异步发送
            :param to=None:
            :param subject="subject":
            :param contents=[]:
        """
        thread = Thread(target=self.send, args=[to, subject, contents])
        thread.start()


if __name__ == "__main__":
    import json, os, sys
    config = {}
    with open(os.path.expanduser("~/.mail")) as f:
        config = json.loads(f.read().strip())

    host = config.get("host", "smtp.qq.com")
    port = config.get("port", 465)
    user = config.get("user", "example@qq.com")
    password = config.get("password", "password")   

    subject = 'Test mail subject'
    if len(sys.argv) > 1:
        subject = sys.argv[1]
    body = "Test mail"
    if len(sys.argv) > 2:
        body = sys.argv[2]
    elif len(sys.argv) > 1:
        body = subject

    receivers = [user]
    client = MailClient(host=host, port=port, user=user, password=password)
    print('发送邮件 start')
    client.send(to=receivers, subject=subject, contents=[body])
    print('发送邮件 end')

