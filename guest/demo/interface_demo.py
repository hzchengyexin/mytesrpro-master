from zope.interface import interface
from zope.interface.declarations import implementer
#定义接口
class IHost(Interface):
	def goodmorning(self,host):
		"""Say good morning to host"""

@implementer(IHost) #继承接口
class Host:
	def goodmorning(self,guest):
		"""Say good morning to guests"""
		return "Good morning, %s!" % guest

if __name__ == '__main__':
	p = Host()
	hi = p.goodmorning('Tom')
	print(hi)