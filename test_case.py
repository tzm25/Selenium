from selenium import webdriver
import unittest 

class testcase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/home/void/Selenium/chromedriver")
        self.driver.get("https://www.udemy.com/")

    @unittest.SkipTest
    def test_First_case(self):
        print("This is successful")

    
    def test_Second_case(self):
        print("This is also successful")

    @unittest.skip("I fucking want and skip this! So why?")
    def test_Third_case(self):
        print("This will not perform")
    
    @unittest.skipIf(10==9 ,"Numbers are not equal")
    def test_fourth_case(self):
        print("This will not perform")

    def tearDown(self):
        self.driver.close()
        

if __name__== "__main__":
    unittest.main()