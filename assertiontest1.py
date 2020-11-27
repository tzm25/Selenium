from selenium import webdriver
import unittest 

class testcase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/home/void/Selenium/chromedriver")
        self.driver.get("https://www.udemy.com/")

    
    def test_assertion(self):
        title = self.driver.title
        self.assertTrue(title == "Online Courses - Anytime, Anywhere | Udemy")

  

    def tearDown(self):
        self.driver.close()
        

if __name__== "__main__":
    unittest.main()
    
