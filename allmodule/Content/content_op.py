from GLOBAL_USABLE import *
from allmodule.common_module.Now_Edit.new_edit_ele import random_data
from allmodule.Content.content_ele import *
from allmodule.basepage import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
import allure


class Content(BasePage):
    """
    我的内容页面的operation
    """

    # 打开我的内容页面
    def open_ct_url(self):
        with allure.step(f"打开的页面网址是{CONTENT_URL}"):
            self.open(CONTENT_URL)
            # time.sleep(2)
            assert_in_ct = self.wait_ele_text(assert_ct[0], assert_ct[1])
            assert assert_in_ct is True

    def create_ct(self, form_type):
        """

        :param form_type: 1老表单简介页，2新编辑器简介页
        :return:
        """
        with allure.step("点击上传内容按钮"):
            self.locator_with_wait(*push_ct).click()
        self.ct_name = self.current_time() + "自动化内容测试数据"
        with allure.step(f"输入内容昵称{self.ct_name}"):
            self.locator_with_wait(*ct_name).send_keys(self.ct_name)
        with allure.step(f"输入内容标题{self.ct_name}"):
            self.locator_with_wait(*ct_title).send_keys(self.ct_name)
        with allure.step("上传内容封面"):
            self.locator_with_wait_roll(*upload_ct_cover).send_keys(IMAGE)
            self.wait_ele_vanish(LOADING_ELE)
            if form_type == 1:
                with allure.step("设置内容页面"):
                    self.locator_with_wait_roll(*ct_intro_btn).click()
                with allure.step("点击输入框后进行输入"):
                    self.locator_with_wait(*ct_intro_input).click()
                    self.locator_with_wait(*ct_intro_input).send_keys("内容老简介页测试")
                with allure.step("输入完后点击保存"):
                    self.locator_with_wait(*ct_save_intro).click()
            elif form_type == 2:
                pass

        with allure.step("上传资料"):
            self.locator_with_wait_roll(*update_ct_accessory).send_keys(IMAGE)
            self.wait_ele_vanish(LOADING_ELE)
        with allure.step("允许PC端报名下载资料"):
            self.locator_with_wait_roll(*yes_not_download).click()
        with allure.step("点击内容发布按钮"):
            self.locator_with_wait(*release_ct).click()
        with allure.step("点击确认发布按钮"):
            self.locator_with_wait(*sure_release).click()
        with allure.step("判断内容是否新建成功"):
            assert self.locator_with_wait(*assert_ct_create).text == self.ct_name


