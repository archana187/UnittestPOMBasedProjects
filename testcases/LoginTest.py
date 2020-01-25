import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys
sys.path.append("D://PythonProjects// UnittestPOMBasedProject")
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com "
    password="admin"
    driver=webdriver.Chrome(
        #executable_path="..driver\\chromedriver.exe")
        executable_path="E:\WebDrivers\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"webpage title is not working")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\PythonProjects\\ UnittestPOMBasedProject\\reports'))






