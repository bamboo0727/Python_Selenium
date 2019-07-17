from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https:/baidu.com')

first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

# second_url='http://news.baidu.com'
# print("now access %s" %(second_url))
# driver.get(second_url)
#
# print("back to  %s "%(first_url))
# driver.back()
#
# print("forward to  %s"%(second_url))
# driver.forward()
#


driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_xpath("//*[@id='su']").click()
# driver.quit()

size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

# 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见， 返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.quit()
