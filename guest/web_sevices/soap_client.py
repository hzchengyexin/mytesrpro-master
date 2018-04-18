#! /usr/bin/python
# -*- coding:utf-8 -*-

from suds.client import Client

# 使用库suds_jurko：https://bitbucket.org/jurko/suds
# Web Services查询：http://www.webxml.com.cn/zh_cn/web_services.aspx
# 
# 电话号码归属地查询
url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
result = client.service.getMobileCodeInfo('15757166414')
print(result)