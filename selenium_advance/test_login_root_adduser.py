# -*- coding：utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time,pytest,unittest
from selenium.webdriver.support.select import Select

from selenium.webdriver.support import select


class TestHrmAdduser(unittest.TestCase):
    # @pytest.fixture(scope='module',autouse=True)
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="F:\\hzq\\untitled自动化测试\\dirver\\report\\chromedriver.exe")
        cls.driver.get("http://59.110.52.156/orangehrm/symfony/web/index.php/auth/login")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.maximize_window

    def setUp(self):
        self.driver.find_element_by_id("txtUsername").send_keys("root")
        #把所有定位方法封装find_element（定位方式，定位值）
        self.driver.find_element(By.ID,"txtPassword").send_keys("password1")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        # assert 'Welcome无情' == self.driver.find_element(By.ID,"welcome")
    def test_adduser(self):
        menu_admin_viewAdminModule = self.driver.find_element_by_id("menu_admin_viewAdminModule")
        menu_admin_UserManagement = self.driver.find_element_by_id("menu_admin_UserManagement")
        menu_admin_viewSystemUsers = self.driver.find_element_by_id('menu_admin_viewSystemUsers')
        ActionChains(self.driver) \
            .move_to_element(menu_admin_viewAdminModule) \
            .move_to_element(menu_admin_UserManagement) \
            .click(menu_admin_viewSystemUsers).perform()
        # assert '用户名' in self.driver.page_source
        self.driver.find_element_by_id("btnAdd").click()
        systemUser_userType=self.driver.find_element_by_id("systemUser_userType")
        Select(systemUser_userType).select_by_value("1")
        time.sleep(2)
        # select(systemUser_userType).select_by_visible_test("管理员")
        # select(systemUser_userType).select_by_index("0")
        # self.driver.find_element_by_id("systemUser_employeeName_empName").send_keys("嘎巴 雷霆")
        # self.driver.find_element_by_id("systemUser_userName").send_keys("rootop")
        # systemUser_status = self.driver.find_element_by_id("systemUser_status")
        # Select(systemUser_status).select_by_index("1")
        # self.driver.find_element_by_id("systemUser_password").send_keys("password1")
        # self.driver.find_element_by_id("systemUser_confirmPassword").send_keys("password1")
        # self.driver.find_element_by_id("btnSave").click()
        # time.sleep(2)
        self.driver.refresh()
        #悬停到个人信息管理列表-员工列表
        #页面向上滚动300
        menu_pim_viewPimModule = self.driver.find_element_by_id('menu_pim_viewPimModule')
        menu_pim_viewEmployeeList= self.driver.find_element_by_id("menu_pim_viewEmployeeList")
        ActionChains(self.driver).move_to_element(menu_pim_viewPimModule).click(menu_pim_viewEmployeeList).perform()
        self.driver.execute_script("window,scrollBy(0,300)")
        time.sleep(5)
        self.driver.find_element_by_id("ohrmList_chkSelectRecord_4").click()
        time.sleep(2)#点击最后一个复选框一起写
        ohrmList_chkSelectRecord=self.driver.find_elements_by_name("ohrmList_chkSelectRecord")
        #循环出来元素，get_attribute('value')
        # for i in ohrmList_chkSelectRecord:
        #     print(ohrmList_chkSelectRecord.__getattribute__('value'))
        ohrmList_chkSelectRecord[-1].click()
        self.driver






