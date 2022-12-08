from time import sleep

import allure

from allmodule.ContentCenter.contentcenter_op import ContentCenter
from allmodule.Login.login_op import login


@allure.epic("交互中心模块")
@allure.feature("交互中心表单测试模块")
class Test_contentCenter:
    @allure.story("交互中心创建后报名")
    @allure.title("交互中心创建后报名报名历程")
    def setup_class(self):
        pass

    def teardown(self):
        with allure.step("删除表单"):
            self.CC.del_cc()

    def test_contentcenter_create_new_form_apply(self, browser):
        """
        测试用例描述：
        测试步骤：
                1、先登录
                2、进入到交互中心表单列表
                3、创建交互中心表单
                4、设置报名表单
                5、报名
        """
        # 前置操作 登录
        # with allure.step("登录"):
        #     login(browser)
        # 实例化对象
        self.CC = ContentCenter(browser)
        with allure.step("打开交互中心表单列表页面"):
            self.CC.open_cc()
        with allure.step("创建交互中心表单并设置表单内容"):
            self.CC.create_just_set_form()
        with allure.step("提交表单"):
            self.CC.apply_cc_form()

