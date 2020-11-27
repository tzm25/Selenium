from selenium import webdriver

path = "/home/void/Selenium-Course/chromedriver"

driver = webdriver.Chrome(path)

driver.get("https://www.udemy.com")
