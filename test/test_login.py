# -*- coding：utf-8 -*-
import unittest
from selenium import webdriver
from pages import base_operate,login_apple
class TestLogin(unittest.TestCase):
    #打开浏览器，输入登录页
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="F:\\hzq\\untitled自动化测试\\dirver\\report\\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://59.110.52.156/orangehrm/symfony/web/index.php/admin/viewJobTitleList")
        #初始化基础页面
        cls.base_page = base_operate.BasePage(cls.driver)

    @unittest.skip
    def test_login_correct(self):
        #初始化登录页（元素定位操作），按测试用例顺序编写代码，在加断言
        login_page=login_apple.LoginPage(self.driver)
        login_page.enter_username("root")
        login_page.enter_password("password2")
        login_page.click_login()
        self.base_page.save_picture("2.png")
        assert 'admin' in login_page.login_sucess_result()

    def test_login_error(self):
        login_page = login_apple.LoginPage(self.driver)
        login_page.enter_username("root")
        login_page.enter_password("password1")
        login_page.click_login()
        self.base_page.save_picture("2.png")
        assert 'admin' in login_page.login_sucess_result()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
