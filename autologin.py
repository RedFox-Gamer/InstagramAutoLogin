from selenium import webdriver
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#Open Instagram's website using geckodriver.exe
#geckodriver.exe should be in the "PATH" variable
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=firefox_capabilities)
driver.get("https://www.instagram.com/")
sleep(2)

#Switch accounts if already logged in
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
sleep(2)

#Enter the defined username
driver.find_element_by_name("username").send_keys("PUT YOUR USERNAME HERE")
sleep(2)

#Enter the defined password
driver.find_element_by_name("password").send_keys("PUT YOUR PASSWORD HERE")
sleep(2)

driver.find_element_by_name("password").send_keys(u'\ue007')
sleep(2)