from GLOBAL_USABLE import *
from allmodule.common_module.Now_Edit.new_edit_ele import random_data
from allmodule.WeBtv.WeBtv_ele import *
from allmodule.basepage import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
import allure
from allmodule.common_module.Now_Edit.new_edit_op import New_Edit


class WebTv_Page(BasePage):
    """
    直播页面的operation
    """

    # 打开直播列表页面
    def open_url(self):
        with allure.step(f"打开的页面网址是{WEBTV_URL}"):
            self.open(WEBTV_URL)
            # time.sleep(2)
            assert_in_tv = self.wait_ele_text(assert_tv[0], assert_tv[1])
            assert assert_in_tv is True

    # # 直播操作 设置表单 功能
    # def tv_op(self):
    #     self.locators(*setTVForm[0], setTVForm[1]).click()

    # 新建直播
    def create_tv(self):
        # 直播页面点击新建直播
        with allure.step("直播页面点击新建直播"):
            self.locator_with_wait(*new_WebTv).click()
        # 选择类型
        with allure.step("选择类型"):
            self.locator_with_wait(*TvType).click()
            self.locator_with_wait(*S_TvType).click()
        # 输入直播地址
        with allure.step("输入直播地址"):
            self.locator_with_wait(*txtTvUrl).send_keys(txt_url)
        # 直播名字
        self.tv_name = self.current_time() + "自动化直播测试数据"
        with allure.step(f"直播名字是{self.tv_name}"):
            self.locator_with_wait(*TvName).send_keys(self.tv_name)
        # 直播开始时间
        with allure.step(f"设置直播开始时间:{self.js_time_ele()}"):
            self.js_time_ele(create_time)
        # 直播结束时间
        with allure.step(f"设置直播结束时间:{self.js_time_ele(t=7)}"):
            self.js_time_ele(e_id=end_time, t=7)
        # 上传封面图片,这里用的是input标签，可以直接输入文件路径
        with allure.step(f"上传封面图片:{IMAGE}"):
            self.locator_with_wait_roll(*upload_tv_img).send_keys(IMAGE)
            time.sleep(2)
            # self.wait_ele_visible("xpath", "//*[text()='上传中...']")
        # 输入简介页内容
        with allure.step("点击设置内容简介页"):
            self.roll_locator_ele(*intro_btn).click()
            # 等待输入框出现
            self.wait_ele_visible("xpath", "//*[@id='ma-LivePageSetting']")
        with allure.step("点击输入框后进行输入"):
            self.locator_with_wait(*intro_input).click()
            self.locator_with_wait(*intro_input).send_keys("直播测试")
        with allure.step("输入完后点击保存"):
            self.locator_with_wait(*save_intro).click()
            # 发布直播
        with allure.step("发布直播"):
            self.roll_locator_ele(*save_webtv).click()
        # 点击弹框里的完成
        with allure.step("点击完成"):
            self.locator_with_wait(*finish_btn).click()
        # 断言创建的直播是否在直播列表里
        assert self.tv_name == self.locators(*assert_newtv[0], assert_newtv[1]).text
        # time.sleep(5)

    def set_tv_form(self):
        """
        前置条件:1.需要是新创建的直播没有表单，
                2.在直播列表才能使用该方法
        """
        with allure.step("点击设置表单按钮"):
            self.locators(*setTVForm).click()
        with allure.step("点击设置表单内容按钮"):
            self.locator_with_wait(*setTVForm_content).click()
        with allure.step("新建表单选择内型：新编辑器表单"):
            self.locator_with_wait(*new_edit).click()
        # with allure.step("选择表单模板"):
        #     self.locator_with_wait(*new_Form).click()
        # # time.sleep(2)
        # # self.wait_ele_visible(*wait_new_edit_ele)
        # # self.wait_ele_visible(*add_Form[0])
        # self.wait.until_not(EC.visibility_of_element_located(wait_new_edit_ele))
        with allure.step("设置新编辑器表单内容操作"):
            New_Edit(self.driver).set_new_edit_op()
        self.wait.until(EC.title_is("直播表单"))

    # @allure.step("报名直播表单")
    def apply_tv_form(self):
        self.open(WEBTV_URL)
        self.locators(*setTVForm).click()
        # 获取直播报名地址,通过属性value获取url
        tv_url = self.locator_with_wait(*gina_tv_url).get_attribute("value")
        with allure.step("打開直播表单页"):
            self.driver.get(tv_url)
        with allure.step("报名"):
            New_Edit(self.driver).write_new_edit_op(random_data).apply_form()

    # @allure.step("在直播列表删除直播")
    def del_tv(self):
        self.open(WEBTV_URL)
        with allure.step("删除直播"):
            # 防止删错直播
            assert self.tv_name == self.locators(*assert_newtv[0], assert_newtv[1]).text
            self.locator_with_wait(*delTV).click()
            self.locator_with_wait(*del_bnt).click()
        # self.driver.refresh()
        # assert_tv_name = self.locators(*assert_newtv[0], assert_newtv[1])
        # # print(assert_tv_name.text, self.tv_name)
        # assert assert_tv_name.text != self.tv_name
        with allure.step("断言测试的直播是否删除成功"):
            assert self.locator_with_wait(*(assert_del_tv[0])).text == assert_del_tv[1]
