from selenium import webdriver
import unittest 

class testcase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/home/void/Selenium/chromedriver")
        self.driver.get("https://www.udemy.com/")

        #self.assertIsNone(self.driver)
        self.assertIsNotNone(self.driver)
    
    def test_assertion(self):
        title = self.driver.current_url
        self.assertTrue(title == "https://www.udemy.com/")
   
    def test_assertion2(self):
        title = self.driver.current_url
        self.assertEqual("https://www.udemy.com/", title, "The title is not matched")
    
    def test_assertion3(self):
        title = self.driver.current_url
        self.assertNotEqual("https://www.google.com",title,"U fucking mismatched")

    def test_assertion4(self):
        self.assertGreater(100,10)
        self.assertGreaterEqual(100,100)
        self.assertLess(10,100)
        self.assertLessEqual(10,10)
  

    def tearDown(self):
        self.driver.close()
        

if __name__== "__main__":
    unittest.main()
    
