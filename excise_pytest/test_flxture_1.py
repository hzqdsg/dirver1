# -*- coding：utf-8 -*-
'''
UI自动化全部打开浏览器，只执行一次

'''
import pytest


def test_search():
    print("root")
@pytest.mark.usefixtures("login")
def test_cart():
    print("pim")
@pytest.mark.usefixtures("login")
def test_pay():
    print("job")
if __name__ == '__main__':
        pytest.main()