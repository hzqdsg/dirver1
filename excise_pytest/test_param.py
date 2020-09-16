# -*- coding：utf-8 -*-
import pytest
#通过fixyure自带的参数进行数据驱动，形参必须是request
@pytest.fixture(params=[1,2,3,'dog'])
def data_param(request):
    return request.param
#测试方法需要一些数据通过装饰器的方式加载数据
def test_fixyure_param(data_param):
    print(data_param)


