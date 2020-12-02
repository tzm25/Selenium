from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class twitter_bot():
    def __init__(self, phonenumber, password):
        self.phonenumber = phonenumber
        self.password = password
        self.driver = webdriver.Chrome("/home/void/Selenium/chromedriver")
        self.driver.maximize_window()

    def login(self):
        driver = self.driver
        driver.get("http://twitter.com/")
        sleep(4)
        user=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/label/div/div[2]/div/input')
        user.clear()
        user.send_keys(self.phonenumber)
        passw=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[2]/div/label/div/div[2]/div/input')
        passw.clear()
        passw.send_keys(self.password)
        click_ = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[3]/div')
        click_.click()
        sleep(3)

    def liketweet(self,searchfor):
        driver = self.driver
        driver.get("https://twitter.com/search?q="+searchfor+"&src=typed_query")
        sleep(3)
        
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(3)
        #driver.find_element_by_tag_name("body").send_keys(Keys.F + Keys.LEFT)
        likes = driver.find_elements_by_xpath('//div[@data-testid="like"]')
        for like in likes:
            like.click()
            sleep(3)

        

searchfor = "python"

phonenumber= "09777789112"
password = "chochoaung"
twitter = twitter_bot(phonenumber,password)
twitter.login()

twitter.liketweet(searchfor)


