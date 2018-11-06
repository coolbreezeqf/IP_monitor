#!/usr/bin/python
# -*- coding:utf8 -*-
# author: colbrze430@gmail.com
# date: 2018.05.31

# 调用 阿里云SDK
'''
https://help.aliyun.com/document_detail/53090.html?spm=5176.11122631.962077.5.22722a6auD6fAk
1. 安装 SDK
python2:
    pip install aliyun-python-sdk-core
    pip install aliyun-python-sdk-ecs
python3:
    pip install aliyun-python-sdk-core-v3
    pip install aliyun-python-sdk-ecs

域名 SDK:
    pip install aliyun-python-sdk-domain (误)
    pip install aliyun-python-sdk-alidns

2. 获取 Region ID、AccessKey ID和AccessKey Secret
- [Region ID](https://www.alibabacloud.com/help/zh/doc-detail/40654.htm)

'''
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest

import json


class DomainTool:
    def __init__(self, client, domain):
        self.client = client
        self.domain = domain
        self.records = []

    def get_records(self):
        r = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
        r.set_DomainName(self.domain)
        res = self.client.do_action_with_exception(r)
        records = json.loads(res)['DomainRecords']['Record']
        for record in records:
            if record['Type'] == 'A':
                self.records.append(record)

    def get_ip(self):
        if not self.records:
            self.get_records()
        ip = self.records[0]['Value']
        print(ip)
        return ip

    def change_ip(self, ip):
        if not self.records:
            self.get_records()
        for record in self.records:
            r = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
            r.set_RecordId(record['RecordId'])
            r.set_RR(record['RR'])
            r.set_Type(record['Type'])
            r.set_Value(ip)
            try:
                res = self.client.do_action_with_exception(r)
                print(res)
            except Exception as e:
                print(e)
                raise


if __name__ == '__main__':
    from aliyunconfig import Config
    client = AcsClient(Config.AccessKeyId, Config.Secret)
    c = DomainTool(client, Config.Domain)
    print(c.domain)
    print(c.get_ip())
    c.change_ip('1.1.1.1')
    print(c.get_ip())
