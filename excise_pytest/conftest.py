# # -*- coding：utf-8 -*-
# '''
# 这个文件是哪级对哪级共享数据
# '''
# #login是登录，要加到购物车和支付之前，是他们依赖方法 fixture
# # @pytest.fixture()
# import pytest
# @pytest.fixture(scope='module',autouse=True)
# def open_browser():
#     print("打开浏览器，登录")
#     yield
#     print("关闭浏览器")
# @pytest.fixture()
# def login():
#     print("登录")