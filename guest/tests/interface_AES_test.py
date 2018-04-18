#! /usr/bin/python
# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
import base64
import requests
import unittest
import json

class AESTest(unittest.TestCase):
	"""AES加密后的接口测试用例"""
	def setUp(self):
		""""初始化测试参数"""
		BS = 16
		self.pad = lambda s:s+(BS - len(s) % BS) * chr(BS - len(s) % BS) #使用lambda定义匿名函数来对字符串进行补足，使其长度变为16、24、32位
		self.base_url = "http://127.0.0.1:8000/api/sec_get_guest_list/"
		self.app_key = "W7v4D60fds2Cmk2U" #定义好app_key,app_key是密钥，只能告诉给合法的接口调用者
	def encryptBase64(self,src):
		return base64.urlsafe_b64encode(src)
	def encryptAES(self,src,key):
		"""生成AES密文"""
		iv = b"1172311105789011" #定义好iv，iv是保密的，必须为16位
		cryptor = AES.new(key,AES,MODE_CBC,iv)
		ciphertext = cryptor.encrypt(self.pad(src)) #通过encrypt()方法对src（Json格式的接口参数）生成加密字符串
		return self.encryptBase64(ciphertext) #通过envrypt()方法生成的加密字符串太长不适合传输，于是，通过base64模块的urlsafe_b64encode()方法对AES加密字符串进行二次加密
	def test_case_interface(self):
		"""测试AES加密的接口"""
		payload = ('eid';1,'phone':'18011001100') #使用字典格式来存放接口参数
		# 加密过程
		encode = self.encryptAES(json.dumps(payload),self.app_key.decode())  # 通过json.dumps()方法将payload字典转化为JSON格式，和app_key一起做为encryptAES()方法的参数，用于生成AES加密字符串
		r = requests.post(self.base_url,data = {'data':encoded}) #将加密后的字符串作为data参数发送到接口请求
		result = r.json()
		self.assertEqual(result['result'],200)
		self.assertEqual(result['message'],'success')
	def test_get_guest_list_request_error(self):
		"""测试嘉宾查询接口：eid为空"""
		payload = {'eid': '', 'phone': ''}
		encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
		r = requests.post(self.base_url, data={"data": encoded})
		result = r.json()
		self.assertEqual(result['status'], 10011)
		self.assertEqual(result['message'], 'request error')
	def test_get_guest_list_eid_null(self):
		"""测试嘉宾查询接口：phone为空"""
		payload = {'eid': '', 'phone': '18011001100'}
		encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
		r = requests.post(self.base_url, data={"data": encoded})
		result = r.json()
		self.assertEqual(result['status'], 10021)
		self.assertEqual(result['message'], 'eid cannot be empty')
	def test_get_guest_list_eid_error(self):
		"""根据eid查询结果为空"""
		payload = {'eid': '901', 'phone': ''}
		encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
		r = requests.post(self.base_url, data={"data": encoded})
		result = r.json()
		self.assertEqual(result['status'], 10022)
		self.assertEqual(result['message'], 'query result is empty')
	def test_get_guest_list_eid_success(self):
		"""根据eid查询结果成功"""
		payload = {'eid': '1', 'phone': '18011001100'}
		encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
		r = requests.post(self.base_url, data={"data": encoded})
		result = r.json()
		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'success')
		self.assertEqual(result['data'][0]['realname'], 'alen')
		self.assertEqual(result['data'][0]['phone'], '18011001100')
	def test_get_event_list_eid_phone_null(self):
		"""根据eid和phone查询结果为空"""
		payload = {'eid': '200', 'phone': '10000000000'}
		encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
		r = requests.post(self.base_url, data={"data": encoded})
		result = r.json()
		self.assertEqual(result['status'], 10022)
		self.assertEqual(result['message'], 'query result is empty')
	def test_get_event_list_eid_phone_success(self):
		"""根据eid和phone查询结果成功"""
		payload = {'eid': '1', 'phone': '18011001100'}
		encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
		r = requests.post(self.base_url, data={"data": encoded})
		result = r.json()
		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'success')
		self.assertEqual(result['data']['realname'], 'alen')
		self.assertEqual(result['data']['phone'], '18011001100')

if __name__ == '__main__':
	unittest.main()