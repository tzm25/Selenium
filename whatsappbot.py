import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("/home/void/Selenium/chromedriver")

driver.get("https://web.whatsapp.com")
driver.maximize_window()
sleep(7)

print("Please scan the QR code")
sleep(7)

search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_box.send_keys("CHo")
search_box.send_keys(Keys.ENTER)
sleep(5)

type_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
type_msg.send_keys("Hello! I'm Thant Zin Moe. This message is sending from whatsapp testing bot")
type_msg.send_keys(Keys.ENTER)
