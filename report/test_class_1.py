# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Hrm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='F:\\hzq\\untitled自动化测试\dirver\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://59.110.52.156/"


    def test_sele(self):
        driver = self.driver
        driver.get("http://59.110.52.156/orangehrm/symfony/web/index.php/auth/login")
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("root")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("password1")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_xpath("//a[@id='menu_admin_viewAdminModule']/b").click()
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("systemUser_employeeName_empName").click()
        driver.find_element_by_id("systemUser_employeeName_empName").clear()
        driver.find_element_by_id("systemUser_employeeName_empName").send_keys(u"嘎巴")
        driver.find_element_by_xpath("//div[4]/ul/li").click()
        driver.find_element_by_id("systemUser_userName").click()
        driver.find_element_by_id("systemUser_userName").clear()
        driver.find_element_by_id("systemUser_userName").send_keys("root")
        driver.find_element_by_id("systemUser_password").clear()
        driver.find_element_by_id("systemUser_password").send_keys("password1")
        driver.find_element_by_id("systemUser_userName").click()
        driver.find_element_by_id("systemUser_userName").clear()
        driver.find_element_by_id("systemUser_userName").send_keys("rootp")
        driver.find_element_by_id("systemUser_confirmPassword").click()
        driver.find_element_by_id("systemUser_confirmPassword").clear()
        driver.find_element_by_id("systemUser_confirmPassword").send_keys("password1")
        driver.find_element_by_id("btnSave").click()
        driver.find_element_by_id("menu_admin_viewJobTitleList").click()
        driver.find_element_by_id("menu_admin_viewJobTitleList").click()
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("jobTitle_jobTitle").click()
        driver.find_element_by_id("jobTitle_jobTitle").click()
        driver.find_element_by_id("jobTitle_jobTitle").click()
        driver.find_element_by_id("jobTitle_jobTitle").click()
        driver.find_element_by_id("jobTitle_jobTitle").click()
        driver.find_element_by_id("jobTitle_jobTitle").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=jobTitle_jobTitle | ]]
        driver.find_element_by_id("jobTitle_jobTitle").click()
        driver.find_element_by_id("jobTitle_jobTitle").clear()
        driver.find_element_by_id("jobTitle_jobTitle").send_keys(u"经理")
        driver.find_element_by_id("btnSave").click()
        driver.find_element_by_id("btnSave").click()
        driver.find_element_by_id("menu_recruitment_viewJobVacancy").click()
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("addJobVacancy_jobTitle").click()
        Select(driver.find_element_by_id("addJobVacancy_jobTitle")).select_by_visible_text(u"经理")
        driver.find_element_by_id("addJobVacancy_jobTitle").click()
        driver.find_element_by_id("addJobVacancy_name").click()
        driver.find_element_by_id("addJobVacancy_name").clear()
        driver.find_element_by_id("addJobVacancy_name").send_keys(u"哈拉少")
        driver.find_element_by_id("addJobVacancy_hiringManager").click()
        driver.find_element_by_id("addJobVacancy_hiringManager").clear()
        driver.find_element_by_id("addJobVacancy_hiringManager").send_keys(u"嘎巴")
        driver.find_element_by_xpath("//div[4]/ul/li").click()
        driver.find_element_by_id("btnSave").click()
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()
        driver.close()



if __name__ == "__main__":
    unittest.main()

