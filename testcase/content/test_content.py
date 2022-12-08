import allure
from allmodule.Content.content_op import *


@allure.epic("内容模块")
@allure.feature("内容表单测试模块")
class Test_content:
    @allure.story("内容创建后报名")
    @allure.title("内容创建后报名报名历程")
    def setup_class(self):
        pass

    def teardown(self):
        pass

    def test_content_create_old_intro_old_form_apply(self, browser):
        """
        测试用例描述：内容老简介页、老报名表单
        测试步骤：
                1、先登录
                2、进入到我的内容列表
                3、报名
        """
        self.Ct = Content(browser)
        self.Ct.open_ct_url()
        self.Ct.create_ct(1)
