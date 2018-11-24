import os,sys
sys.path.append(os.getcwd())
import allure,pytest



class Test():
    #@allure.step("描述语句")  --只能修饰函数
    # allure.attach("描述", "登录")  里边两个是必传参数  --针对函数里的描述
    @allure.step("登录操作")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login(self):
      # allure.attach("描述", "登录")  里边两个是必传参数
        allure.attach("描述","登录")
        print("登录")

    # @allure.step("退出操作")
    # @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_exit(self):
        allure.attach("描述", "登录")
        print("退出")

    # @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_03(self):
        allure.attach("描述", "03")
        try:
            print("退出")
            assert 0
        except:
            pass

