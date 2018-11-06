#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os

from dingdingsdk import DingdingClient
from mail import MailClient
from aliyunsdk import AcsClient, DomainTool
from ip_monitor import Monitor

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(DIR_PATH, "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

dingding_client = DingdingClient(config.get("dingding", "token"))
mail_client = MailClient(**config["mail"])
alilyun_client = AcsClient(config.get("aliyun", "accesskeyid"),
                              config.get("aliyun", "secret"))
domain_tool = DomainTool(alilyun_client, config.get("aliyun", "domain"))
ipmonitor = Monitor()


def main():
    if ipmonitor.isChange():
        ip = ipmonitor.current_ip
        domain_tool.change_ip(ip)
        dingding_client.send_markdown('IP 更变通知', '> **机器ip变更为'+ip)
        mail_client.send(to=config.get("mail", "receivers").strip().split(','),
                         subject="IP 更变通知", contents=["IP 地址更变为" + ip])


if __name__ == "__main__":
    main()
