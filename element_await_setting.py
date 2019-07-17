#
# 显式等待使WebdDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）。
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# element = WebDriverWait(driver, 5, 0.5).until(
#                       EC.presence_of_element_located((By.ID, "kw"))
#                       )
# element.send_keys('selenium')
# driver.quit()
# WebDriverWait类是由WebDirver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。具体格式如下：
#
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
# driver ：浏览器驱动。
#
# timeout ：最长超时时间，默认以秒为单位。
#
# poll_frequency ：检测的间隔（步长）时间，默认为0.5S。
#
# ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。
#
# WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。
#
# until(method, message=‘’)
# 调用该方法提供的驱动程序作为一个参数，直到返回值为True。
#
# until_not(method, message=‘’)
# 调用该方法提供的驱动程序作为一个参数，直到返回值为False。
#
# 在本例中，通过as关键字将expected_conditions 重命名为EC，并调用presence_of_element_located()方法判断元素是否存在。


# WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0。它的用法相对来说要简单得多。
#
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from time import ctime
#
# driver = webdriver.Firefox()
#
# # 设置隐式等待为10秒
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
#
# try:
#     print(ctime())
#     driver.find_element_by_id("kw22").send_keys('selenium')
# except NoSuchElementException as e:
#     print(e)
# finally:
#     print(ctime())
#     driver.quit()