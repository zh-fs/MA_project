from time import sleep
import allure
# from selenium import webdriver
from allmodule.Login.login_op import login
from allmodule.WeBtv.WeBtv_op import WebTv_Page


@allure.epic("直播模块")
@allure.feature("直播测试模块")
class Test_WebTv:
    @allure.story("直播创建后报名")
    @allure.title("直播【老简介页新编辑器表单】创建报名历程")
    def setup_class(self):
        pass

    def teardown(self):
        with allure.step("删除直播"):
            self.WP.del_tv()
            
    def test_old_webtv_create_apply(self, browser):
        """
        测试用例描述：
        测试步骤：
                1、先登录
                2、进入到直播列表
                3、创建直播
                4、设置直播报名表单
                5、报名
        """
        # # 前置操作 登录
        # with allure.step("登录"):
        #     login(browser)
        # 实例对象
        self.WP = WebTv_Page(browser)
        # 打开直播页面
        with allure.step("打开直播列表页面"):
            self.WP.open_url()
        with allure.step("新建直播"):
            self.WP.create_tv()
        with allure.step("设置表单"):
            self.WP.set_tv_form()
        with allure.step("填写表单且报名"):
            self.WP.apply_tv_form()


# if __name__ == '__main__':
#     test_webtv(webdriver.Chrome())
