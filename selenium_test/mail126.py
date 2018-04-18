from selenium import webdriver

#登录
def login():
	driver.find_element_by_id("idInput").clear()
	driver.find_element_by_id("idInput").send_keys("username")
	driver.find_element_by_id("pwsInput").clear()
	driver.find_element_by_id("pwsInput").send_keys("password")
	driver.find_element_by_id("loginBtn").click()

#退出
def logout():
	driver.find_element_by_link_text("退出").click()
	driver.quit()

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.126.com")
login()

#收信
#写信

logout()