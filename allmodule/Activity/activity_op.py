from time import sleep

from GLOBAL_USABLE import *
from allmodule.Activity.activity_ele import *
from allmodule.common_module.Now_Edit.new_edit_ele import random_data
from allmodule.common_module.Now_Edit.new_edit_op import New_Edit
from allmodule.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

from allmodule.common_module.old_form_one.old_form_op import Old_Edit


class Activity_Page(BasePage):
    """
    活动列表operation
    """
    def open_ac(self):
        with allure.step(f"打开的页面网址是{ACTIVITY_URL}"):
            self.open(ACTIVITY_URL)
        assert_in_tv = self.wait_ele_text(assert_ac[0], assert_ac[1])
        assert assert_in_tv is True

    # 新建活动
    def create_ac(self):
        with allure.step("活动页面点击新建活动按钮"):
            self.locator_with_wait(*create_ac).click()
        self.activity_name = self.current_time() + "自动化活动测试数据"
        with allure.step(f"输入活动名称：{self.activity_name}"):
            self.locator_with_wait(*ac_name).send_keys(self.activity_name)
        with allure.step(f"选择活动分类"):
            self.locator_with_wait(*ac_type_click).click()
            # 默认选择第一个分类
            self.locator_with_wait(*ac_type_sel).click()
        with allure.step(f"设置活动开始时间:{self.js_time_ele()}"):
            self.js_time_ele(e_id=ac_start_time)
        with allure.step(f"设置活动结束时间：{self.js_time_ele(t=7)}"):
            self.js_time_ele(e_id=ac_end_time, t=7)
        with allure.step("点击确定添加活动按钮"):
            self.locator_with_wait(*ac_sure_bnt).click()

    def create_ac_form(self, form_type):
        """

        :param form_type: 1活动老表单类型（1）、2活动老表单类型（2）、3新编辑器表单
        :return:
        """
        with allure.step("点击活动创建表单"):
            self.locator_with_wait(*ac_create_form).click()
        if form_type == 1:
            with allure.step("选择创建表单类型"):
                self.locator_with_wait(*ac_old_form01_type).click()
            with allure.step("设置活动报名表单:活动老表单1"):
                Old_Edit(self.driver).save_form()
        # elif form_type == 2:
        #     with allure.step("选择创建表单类型"):
        #         self.locator_with_wait(*ac_old_form02_type).click()
        #     with allure.step("设置活动报名表单:活动老表单2"):
        #         New_Edit(self.driver).set_new_edit_op()
        elif form_type == 3:
            with allure.step("选择创建表单类型"):
                self.locator_with_wait(*ac_new_form_type).click()
            with allure.step("设置活动报名表单:新编辑器表单"):
                New_Edit(self.driver).set_new_edit_op()
        self.wait.until(EC.title_is("宣传表单"))

    def apply_ac_form(self):
        self.open_ac()
        with allure.step("点击活动链接进入活动报名页"):
            self.locator_with_wait(*ac_link_click).click()
        with allure.step("报名"):
            New_Edit(self.driver).write_new_edit_op(random_data).apply_form()

    def del_ac(self):
        self.open_ac()
        with allure.step("点击删除活动"):
            self.locator_with_wait(*ac_del).click()
            self.locator_with_wait(*ac_del_sure).click()
        # with allure.step("断言活动是否删除"):
        #     assert self.locator_with_wait(*assert_del_ac).text != self.activity_name

