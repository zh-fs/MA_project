from time import sleep

import allure
import pytest
from allmodule.Activity.activity_op import Activity_Page
from allmodule.Login.login_op import login


@allure.epic("活动模块")
@allure.feature("活动测试模块")
class Test_WebTv:
    @allure.story("活动创建后报名")
    @allure.title("活动【新编辑器表单】创建报名历程")
    def setup_class(self):
        pass
    
    def teardown(self):
        with allure.step("删除表单"):
            self.AP.del_ac()
            
    def test_activity_create_new_form_apply(self, browser):
        """
        测试用例描述：
        测试步骤：
                1、先登录
                2、进入到活动列表
                3、创建活动
                4、设置新编辑器活动报名表单
                5、报名
        """
        # 前置操作 登录
        # with allure.step("登录"):
        #     login(browser)
        # 实例化对象
        self.AP = Activity_Page(browser)
        with allure.step("打开活动列表页面"):
            self.AP.open_ac()
        with allure.step("创建活动"):
            self.AP.create_ac()
        with allure.step("设置表单"):
            self.AP.create_ac_form(3)
        with allure.step("提交表单"):
            self.AP.apply_ac_form()


