# -*- coding：utf-8 -*-
#登录要进行的操作，输入，点击
from selenium.webdriver.support.wait import WebDriverWait
from pages.Locators import LoginPageLocators, WelcomePageLocators
from pages.base_operate import BasePage

class LoginPage(BasePage):
    #用户输入用户名，密码点击登录
    def enter_username(self,username):
        #加个智能等待，点击用户名，文本框清除，输入root
        WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*LoginPageLocators.txtUsername))
        usernameele=self.driver.find_element(LoginPageLocators.txtUsername)
        usernameele.click()
        usernameele.clear()
        usernameele.send_keys(username)
    def enter_password(self,password):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*LoginPageLocators.txtPassword))
        passwordele=self.driver.find_element(LoginPageLocators.txtPassword)
        passwordele.click()
        passwordele.clear()
        passwordele.send_keys(password)
    def click_login(self):
        clickele=self.driver.find_element(*LoginPageLocators.btnLogin)
        clickele.click()
    def login_sucess_result(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*WelcomePageLocators.welcome))
        return self.driver.find_element(*WelcomePageLocators.welcome).text


