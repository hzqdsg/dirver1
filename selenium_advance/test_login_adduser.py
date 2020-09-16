# -*- coding：utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time,pytest
class TestHrmAdduser(object):
    # @pytest.fixture(scope='module',autouse=True)
    @pytest.fixture(scope='module')
    def test_aopenbrowser(self):
        self.driver=webdriver.Chrome(executable_path="F:\\hzq\\untitled自动化测试\\dirver\\report\\chromedriver.exe")
        self.driver.get("http://59.110.52.156/orangehrm/symfony/web/index.php/auth/login")
        self.driver.maximize_window()
        yield
        self.driver.quit()

    # @pytest.fixture(scope='module', autouse=True)
    @pytest.fixture(scope='module')
    def login1(self):
        self.driver.find_element_by_id("txtUsername").send_keys("root")
        #把所有定位方法封装find_element（定位方式，定位值）
        self.driver.find_element(By.ID,"txtPassword").send_keys("password1")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        assert 'Welcome 无情' == self.driver.find_element(By.ID,"welcome")

    @pytest.mark.usefixtures("login1")
    @pytest.mark.usefixtures("aopenbrpwser")
    def test_adduser(self,aopenbrower):
        self.driver=aopenbrower
        #定位要悬停操作的几个元素，通过链式连接，同时操作几个元素
        menu_admin_viewAdminModule = self.driver.find_element_by_id(By.ID, 'menu_admin_viewAdminModule')
        menu_admin_UserManagement = self.driver.find_element_by_id(By.ID, 'menu_admin_UserManagement')
        menu_admin_viewSystemUser = self.driver.find_element(By.ID, 'menu_admin_viewSystemUser')
        ActionChains(self.driver) \
            .move_to_element(menu_admin_viewAdminModule) \
            .move_to_element(menu_admin_UserManagement) \
            .move_to_element(menu_admin_viewSystemUser)


