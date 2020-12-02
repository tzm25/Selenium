import selenium
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome("/home/void/Selenium/chromedriver")

driver.get("https://demo.magentocommerce.com")
driver.maximize_window()
sleep(5)


search = driver.find_element_by_xpath('//*[@id="block-header"]/ul/li[7]/a')
search.click()
sleep(7)

type_ = driver.find_element_by_xpath('//*[@id="edit-keys"]')
type_.click()
type_.clear()
sleep(2)
type_.send_keys("phones")
sleep(2)
type_.submit()