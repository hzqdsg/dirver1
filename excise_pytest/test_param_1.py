# -*- coding：utf-8 -*
#不使用fixture，直接用paramlize进行数据驱动
import pytest



@pytest.mark.parametrize("num1,num2,result",[[1,2,3],[2,3,5],[5,5,10],[6,2,8]],ids=["10以内","10以外","负数","小数"])
def test_coculator(num1,num2,result):
    assert  num1+num2 == result