#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 钉钉机器人
# 参考文档：https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.45484a97kJNZ0S&treeId=257&articleId=105735&docType=1
import json

import requests

class DingdingClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://oapi.dingtalk.com/robot/send?access_token="

    def send_markdown(self, title, body):
        markdown = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": body
            }
        }
        headers = {'Content-Type': 'application/json'}
        url = self.base_url + self.token
        response = requests.post(url, data=json.dumps(markdown), headers=headers).json()
        code = response["errcode"]
        if code == 0:
            print("发送成功: " + title)
        else:
            print("发送失败: " + str(code))
        return code


if __name__ == "__main__":
    test_token = "900f0b24920b423d0c98d1493d3bb381de59a5357980121a0fb43ee36c1aaf07"
    DingdingClient(test_token).send_markdown('test', 'test')
