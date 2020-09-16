# -*- coding：utf-8 -*-
class BasePage(object):
    #初始化打开浏览器
    def __init__(self,driver):
        self.driver=driver
    def save_picture(self,filepath):
        self.driver.save_screenshot(filepath)
