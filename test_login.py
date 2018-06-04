# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_login(self):
        success = True
        wd = self.wd
        wd.get("http://impsa.sb-oir.ru/")
        wd.find_element_by_link_text("Личный кабинет").click()
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").send_keys("\\undefined")
        wd.find_element_by_name("USER_LOGIN").click()
        wd.find_element_by_name("USER_LOGIN").send_keys("\\undefined")
        wd.find_element_by_name("Login").click()
        wd.find_element_by_css_selector("span.main-menu__sub-switch").click()
        wd.find_element_by_link_text("Выход").click()
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").send_keys("\\undefined")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
