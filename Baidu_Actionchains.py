from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.cn")

above = driver.find_element_by_xpath("//*[@id='u1']/a[8]")

ActionChains(driver).move_to_element(above).perform()
