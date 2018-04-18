#! /usr/bin/python
# -*- coding:utf-8 -*-

from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

# 使用库suds_jurko：https://bitbucket.org/jurko/suds
# Web Services查询：http://www.webxml.com.cn/zh_cn/web_services.aspx

url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl'
imp = Import('http://www.w3.org/2001/XMLSchema',location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://Webxml.com.cn/')

client = Client(url, plugins=[ImportDoctor(imp)])
result = client.service.getWeatherbyCityName("北京")
print (result)