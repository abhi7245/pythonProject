from selenium import webdriver
import unittest
from sample_test.pages.login_page import loginpage
from sample_test.pages.home_page import homepage

class orangehrm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver=webdriver.Chrome(executable_path="C:/Users/abhi/PycharmProjects/pythonProject1/driver/chromedriver.exe")
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.implicitly_wait(10)
        driver=self.driver
        login=loginpage(driver)
        home=homepage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        home.click_welcome()
        home.slick_logout()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")
