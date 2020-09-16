import pytest,sys
def setup_module():
    print("这是一个文件在开始时执行一次")
def setup_function():
    print("这个方法里的在不在类的每个方法前执行一次")
def test_function_01():
    print("这是不在类中的方法函数01")
def test_function_02():
    print("这是不在类中的方法函数02")
    print(sys.platform)
def teardown_function():
    print("这个方法里的在不在类的每个方法后执行一次")
def setup_module():...
def setup_function():...
def test_function_01():...
def test_function_02():...
def teardown_function():...

class TestClass():
    def setup_class(self):
        print("在类的开始时执行一次")
    def teardown_class(self):
        print("在类的结束时执行一次")
    def setup_method(self):
        print("在有类的每个方法前执行一次，有几个方法执行几次")
    def teardown_method(self):
        print("在有类的每个方法后执行一次，有几个方法执行几次")
    @pytest.mark.xfail
    def test_method_01(self):
        print("这是类中方法01")
        assert 3==2+1
        assert  3>2 == True
        assert 'kind' in 'kindfil'
        assert ['1'] == [1]
    @pytest.mark.skip
    def test_method_02(self):
        print("这是类中方法02")
        assert{'name':'kind','age':20} == {'name':'kind','age':21}
    environment = 'android'
    @pytest.mark.skipif( environment = "android",reason='android平台没有')
    def test_cart_3(self):
        print('这是mac-apple的环境所以不执行')

    @pytest.mark.skipif(sys.platform == 'win32',reason = '不在windows下执行')
    @pytest.mark.skipif(sys.version_info < (3  ,6),reason = '3.7版本以下不执行')
    def test_cart(login):
        print('如果python3.6以下不执行，windows平台不执行，我这个就执行')

    @pytest.mark.skipif(reason="我不想执行了")
    def test_method_03(self):...
        # print('这是类的方法03')
        # assert '*' * 10 == '*' * 5

if __name__ == '__main__':
    pytest.main()