# -*- coding：utf-8 -*-
'''
有三个模块：查询不需要登陆，购物车，支付是要登陆
登录是前提不是测试，setup（）：写的是登录，必须所有模块都是登录

'''
import pytest
#login是登录，要加到购物车和支付之前，是他们依赖方法 fixture
@pytest.fixture()
def login():
    print("使用root/password1已经登录了")
def test_search():
    print("搜索商品")
def test_cart(login):
    print("添加商品到购物车")
def test_pay(login):
    print("支付商品订单")
if __name__ == '__main__':
        pytest.main()