# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re
#-*- coding:utf-8 -*-
#"第一步进行导包"
#在类似加上ddt
#在需要数据测试的方法上file_data文件上传
from ddt import ddt,file_data
from HTMLTestRunner import HTMLTestRunner

@ddt
class test_sele(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'F:\\hzq\\untitled自动化测试\dirver\report\chromedriver.exe')
        # 全局智能等待为30，出现错误，等待30秒，每5秒检查一次，如果30秒到了，还是错误报错。
        cls.driver.implicitly_wait(30)
        cls.base_url = "http://59.110.52.156/"


    def test_sele1(self):
        driver = self.driver
        driver.get("http://59.110.52.156/orangehrm/symfony/web/index.php/admin/viewJobTitleList")
        driver.find_element_by_xpath("//div[@id='divUsername']/span").click()
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_xpath('//*[@id="txtUsername"]').clear()
        driver.find_element_by_id("txtUsername").send_keys("root")  # 输入r用户名
        driver.find_element_by_id("txtPassword").clear()  # 清空密码
        driver.find_element_by_id("txtPassword").send_keys("password1")  # 输入密码
        driver.find_element_by_id("btnLogin").click()  # 提交
        time.sleep(2)
        driver.find_element_by_xpath("//a[@id='menu_admin_viewAdminModule']/b").click()
        driver.find_element_by_id("menu_admin_Job").click()  # 点击管理员job
        driver.find_element_by_id("menu_admin_viewJobTitleList").click()  # 点击JobTitl
        # 是断言
        # self.assertEqual("欢迎admin", driver.find_element_by_id("welcome").text)
        #assert "Welcome无情" == driver.find_element_by_id("welcome").text
        @file_data("login1.yaml")
        def test_sele2(self,job):
            print(job)
            driver = self.driver
            driver.find_element_by_id("btnAdd").click()  # 点击添加
            driver.find_element_by_id("jobTitle_jobTitle").click()  # 点击jobtitle输入框
            driver.find_element_by_id("jobTitle_jobTitle").clear()  # 清空输入框
            driver.find_element_by_id("jobTitle_jobTitle").send_keys(job)  # 填写
            driver.find_element_by_id("btnSave").click()  # 提交
            filename = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 截图以随时间命名
            driver.save_screenshot(str(filename) + "1.png")  # 截图完成页

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # self.assertEqual ( [] , self.verificationErrors )

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    # 通过类名把要测试类及类中方法加载到套件中
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_sele))
    # 执行用例--执行结果保存到html格式报告。
    with open("result1.html", 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title="测试报告",
            description="UI测试"
        )
        runner.run(suite)
