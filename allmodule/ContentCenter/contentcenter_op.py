from GLOBAL_USABLE import *
from allmodule.common_module.Now_Edit.new_edit_ele import random_data
from allmodule.ContentCenter.contentcenter_ele import *
from allmodule.basepage import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
import allure
from allmodule.common_module.Now_Edit.new_edit_op import New_Edit


class ContentCenter(BasePage):
    """
    交互中心页面的operation
    """
    # 打开交互中心页面
    def open_cc(self):
        with allure.step(f"打开的页面网址是{CENTER_FORM_URL}"):
            self.open(CENTER_FORM_URL)
            # time.sleep(2)
            assert_in_cc = self.wait_ele_text(assert_cc[0], assert_cc[1])
            assert assert_in_cc is True

    # 新建交互中心表单
    def create_just_set_form(self):
        with allure.step("点击新建表单按钮"):
            self.locator_with_wait(*new_center_form).click()
        with allure.step("选择表单空白模板"):
            self.locator_with_wait(*CC_new_Form).click()
        self.cc_name = self.current_time() + "自动化交互中心表单测试数据"
        with allure.step(f"交互中心表单名字是{self.cc_name}"):
            self.locator_with_wait(*CC_name).send_keys(self.cc_name)
        with allure.step("点击确定"):
            self.locator_with_wait(*save_Form).click()
            time.sleep(2)
        with allure.step("跳到最后一个窗口"):
            self.switch_end_hand()
        with allure.step("设置新编辑器表单"):
            New_Edit(self.driver).cc_set_new_edit_op()
        assert self.cc_name == self.locators(*assert_cc_name[0], assert_cc_name[1]).text

    def apply_cc_form(self):
        with allure.step("打開交互中心表单页"):
            self.locators(*open_cc_form[0], idx=open_cc_form[1]).click()
        with allure.step("报名"):
            New_Edit(self.driver).write_new_edit_op(random_data).apply_form()

    # @allure.step("在直播列表删除直播")
    def del_cc(self):
        self.open(CENTER_FORM_URL)
        with allure.step("删除交互中心表单"):
            self.locators(*del_cc_form).click()
            self.locator_with_wait(*check_box).click()
            # time.sleep(300)
            self.locator_with_wait(*del_cc_sure).click()
        with allure.step(f"要删除的表单为：{self.locator_with_wait(*(assert_del_cc[0])).text}"):
            pass
        with allure.step("断言测试的交互中心表单是否删除成功"):
            assert self.locator_with_wait(*(assert_del_cc[0])).text == assert_del_cc[1]




