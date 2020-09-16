import pytest,allure,time
from selenium import webdriver
@allure.description("测试百度搜索功能")
@allure.severity("critical")
@allure.story("正确的测试用例")
def test_add_caculation():
    with allure.step("打开浏览器输入百度地址"):
        driver = webdriver.Chrome(executable_path='F:\\hzq\\untitled自动化测试\\dirver\\report\\chromedriver.exe')
    # 全局智能等待为30，出现错误，等待30秒，每5秒检查一次，如果30秒到了，还是错误报错。
    driver.implicitly_wait(30)
    with allure.step("打开网页"):
        driver.get("https://www.baidu.com/")
    with allure.step("点击输入"):
        driver.find_element_by_id("kw").send_keys("水果")
    time.sleep(2)
    with allure.step("点击搜索按钮"):
        driver.find_element_by_id("su").click()
    time.sleep(2)
    with allure.step('截图验证保存到项目中'):
        driver.save_screenshot("./result/1.png")
        allure.attach.file("./result/1.png", attachment_type=allure.attachment_type.PNG)
    with allure.step("退出网页"):
        driver.quit()