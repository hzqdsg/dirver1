# -*- coding：utf-8 -*-
import pytest
#这个是将fixture与paramtrize进行组合，在@pytest.fixture中准备数据
#在@pytest.mark.paramtrize进行数据驱动执行多次
# test_user_data = ["root","dog","cat"]
test_user_data = [{'name':'用户','password':'password1'},
                  {'name': '狗', 'password': 'password1'},
                  {'name': '猫', 'password': 'password1'}]
@pytest.fixture(scope="module")
def login(request):
    #这是接收传入的参数，接收一个参数
    # user = request.param
    # print("\n打开首页准备登录，登录用户：%s" % user)
    # return user
    username = request.param['name']
    password = request.param['password']
    print(f"\打开首页准备登录，登录用户:{username},密码是:{password}")
    return request.param

#这是pytest的参数化数据驱动，indirect=Ture是把login当作函数去执行
@pytest.mark.parametrize("login",test_user_data,indirect=True,ids=["root","dog","cat"])
def test_login(login):
    #登录用例
    # a = login
    # print("测试用例仲login的返回值：%s" % a)
    # assert a != ""
    name = login['name']
    print(f"本次登录的：{name}")
    assert name != ""
