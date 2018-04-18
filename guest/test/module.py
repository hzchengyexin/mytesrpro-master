"""
Author:hzchengyexin
Date:2018/4/4
Describe:实现简单计算器：+、-、*、/、
"""
class Calculator():
	"""实现两个数的加、减、乘、除"""
	def __init__(self, a, b):
		self.a = int(a)
		self.b = int(b)

	# +
	def add(self):
		return self.a + self.b
	def sub(self):
		return self.a - self.b
	def mul(self):
		return self.a * self.b
	def div(self):
		return self.a / self.b