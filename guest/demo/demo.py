class Host(object):
	def goodmorning(self,name):
		"""Say good morning to guests"""
		return "Good Morning, %s!" % name

if __name__ == '__main__':
	h = Host()
	hi = h.goodmorning('zhangsan')
	print(hi)