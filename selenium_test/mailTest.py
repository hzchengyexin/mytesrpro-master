from selenium import webdriver
from public import Login

class LoginTest():
	def __init__(self):
		driver = webdriver.Chrome()
		driver.implicitly_wait(10)
		driver.get("http://www.126.com")
	#admin用户登录
	def test_admin_login(self):
		username = 'admin'
		password = '123'
		login().user_login(self.driver,username,password)
		self.driver.quit()
	#guest用户登录
	def test_guest_login(self):
		username = 'guest'
		password = '321'
		login().user_login(self.driver,username,password)
		self.driver.quit()

LoginTest().test_admin_login()
LoginTest().test_guest_login()