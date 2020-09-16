# -*- coding：utf-8 -*-
import pytest
import allure
#单元自动化测试脚本
@allure.feature("这是加法的计算器，加数{0}与加数{1}相加功能")
def add_caculator(num1,num2):
    sum=num1+num2
    return sum
@allure.feature("加法的计算器测试")
@allure.description("这是加法的计算器，测试加法的各种情况是否正确")
@allure.severity("critical")
@allure.story("正确的测试用例")
@allure.issue("http://59.110.52.156:8081/zentao/my-bug.html","曾经的bug")
@allure.testcase("http://59.110.52.156:8081/zentao/my-testtask.html","这是加法测试用例")
@pytest.mark.parametrize("num1,num2,result",[[1,2,3],[2,3,5],[5,5,10],[6,2,8]],ids=["10以内","10以外","负数","小数"])
def test_coculator(num1,num2,result):
    with allure.step("第一步：调用加法方法"):
        sum=add_caculator(num1,num2)
    with allure.step("第二步：断言加法运算结果与预期结果是否一致"):
        assert  sum==num1+num2



@allure.description("这是加法的计算器，测试加法的各种无效是否正确")
@allure.severity("normal")
@allure.story("无效的测试用例")
@allure.testcase("http://59.110.52.156:8081/zentao/my-testtask.html")
@pytest.mark.parametrize("num1,num2,result", [[1, '2', 3], [2, '', 5], [-5, '#@wg.,,,,,', -1], [6, 'root', 8]],
                             ids=["字符串数字", "空格", "特殊字符", "字母"])
def test_add_caculator_error(num1,num2,result):
    with allure.step("如果错误截图"):
        allure.attach.file("1.png",
                           attachment_type=allure.attachment_type.PNG)
    with allure.step("html网页的漂亮"):
        allure.attach("<html><body>这是我们要测试的加法<script type='text/javascript'>alert('这是一个惊喜');</script></body></html>",
                      "这是个网页", allure.attachment_type.HTML)
    with allure.step("执行了"):
        sum=add_caculator(num1,num2)
        allure.attach("加数1+加数2=", f"{0}+{1}={2}")
        assert sum ==result