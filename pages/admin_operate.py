# -*- coding：utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_operate import BasePage


class AdminUserPage(BasePage):
    # 1、悬停选择admin-用户管理-users进行userlist页面
    def xuanting_user(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*AdminUserPage))

    # 2、点击添加用户
    def click_adduser(self): ...

    # 3、选择用户类型是下拉菜单，index=0是管理员，=1是ESS
    def systemUser_userIype_select(self, index):

    # 4、输入empName员工名字
    def enter_employ_name(self, empName): ...

    # ―4、输入用户名称
    def enter_user_name(self, userName): ...

    # -5.下拉选择用户状态system_statuS=1是启用
    def select(self, index): ...

    # 6、输入密码systemUser_password
    def enter_systemUser_password(self, systemUser_password): ...

    # 7、输入确认密码systemUser_confirmPassword
    def enter_ssystemUser_confirmPassword(self, confirmPassword): ...

    # 8、点击保存
    def click_btnSave(self): ...

    # 9、断言添加成功
    def login_sucess_result(self): ...



