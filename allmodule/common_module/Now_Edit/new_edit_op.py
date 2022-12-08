from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from allmodule.common_module.Now_Edit.new_edit_ele import *
from allmodule.basepage import BasePage
import allure


class New_Edit(BasePage):
    def set_new_edit_op(self):
        with allure.step("选择表单空白模板"):
            self.locator_with_wait(*new_Form).click()
        self.wait.until_not(EC.visibility_of_element_located(wait_new_edit_ele))
        # 选择表单位置
        with allure.step("选择表单位置"):
            self.locators(*add_Form[0], add_Form[1]).click()

        # 选择系统表单
        with allure.step("选择系统表单"):
            self.locator_with_wait(*sel_Form).click()
        # 添加表单
        with allure.step("添加表单"):
            self.locator_with_wait(*Form).click()
        # 获取表单id属性，方便后续报名使用
        # with allure.step("获取表单id属性"):
        #     self.Form_att_id = self.locator_with_wait(*Form_ele).get_attribute("id")
        with allure.step("发布表单"):
            self.locator_with_wait(*release_Form).click()

    # 只让交互中心使用
    def cc_set_new_edit_op(self):

        self.wait_ele_vanish(wait_new_edit_ele)
        # sleep(3)
        # 选择表单位置
        with allure.step("选择表单位置"):
            self.locators(*add_Form[0], add_Form[1]).click()

        # 选择系统表单
        with allure.step("选择系统表单"):
            self.locator_with_wait(*sel_Form).click()
        # 添加表单
        with allure.step("添加表单"):
            self.locator_with_wait(*Form).click()
        # 获取表单id属性，方便后续报名使用
        # with allure.step("获取表单id属性"):
        #     self.Form_att_id = self.locator_with_wait(*Form_ele).get_attribute("id")
        with allure.step("发布表单"):
            self.locator_with_wait(*release_Form).click()

    def write_new_edit_op(self, args):
        with allure.step("跳到最后一个窗口"):
            self.switch_end_hand()
        with allure.step(f"输入报名信息，目前默认是姓名跟电话，姓名为{args[0]}，电话为{args[1]}"):
            for i in range(len(args)):
                # print(len(args))
                # print(args[i])
                # print(args[0][i])
                self.locators(*write_Form, i).clear()
                self.locators(*write_Form, i).send_keys(args[i])
        # 提交表单
        return self

    def apply_form(self):
        with allure.step("提交表单"):
            self.locator_with_wait_roll(*apply_bnt).click()
        with allure.step("断言是否报名成功"):
            assert self.locator_with_wait(*(apply_assert[0])).text == apply_assert[1]



'''  
  # 待完善,智能识别表单字段报名
    def write_form(self):
        lists1 = []
        # lists2 = []
        # lists3 = []
        # 正常输入框输入字段
        lists1.extend(self.wait.until(EC.visibility_of_all_elements_located(("xpath", "//*[@class='mix-form-label w-break']"))))
        # 系统下拉框字段，例如下拉单选
        # lists2.extend(self.wait.until(EC.visibility_of_all_elements_located(("xpath", "//*[@class='mix-theme-title w-break']"))))
        # # 大一点的输入框，例如大文本
        # lists3.extend(self.wait.until(EC.visibility_of_all_elements_located(("xpath", "//*[@class='text mix-form-normal ng-untouched ng-pristine ng-valid']"))))

        # print(lists1)
        # print(len(lists1))
        if lists1 is not False:
            for i in range(len(lists1)):
                if '姓名' in lists1[i].text:
                    self.locator_with_wait("xpath", "//*[@placeholder='请输入姓名']").send_keys(random_name())
                elif "手机号码" in lists1[i].text:
                    self.locator_with_wait("xpath", "//*[@placeholder='请输入手机号码']").send_keys(random_name())
                elif i > 1:
                    if "电子邮箱" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys(random_name() + "@136.com")
                    elif "公司" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("公司")
                    elif "职位" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("职位")
                    elif "部门" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("部门")
                    elif "电话" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("电话")
                    elif "国家" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("国家")
                    elif "省份" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("省份")
                    elif "城市" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("城市")
                    elif "区县" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("区县")
                    elif "地址" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("地址")
                    elif "学历" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("学历")
                    elif "性别" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys("性别")
                    elif "传真" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys()
                    elif "QQ" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys()
                    elif "邮编" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys()
                    elif "微信号" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys()
                    elif "身份证" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys()
                    elif "普通文本" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys()
                    elif "数字" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys()
                    elif "日期" in lists1[i].text:
                        self.locator_with_wait("xpath", f"//form/div[{i+2}]/div/div[2]/input").send_keys()


driver = webdriver.Chrome()
driver.get('https://wx.vipmaillist.com/contentCenter/ContentCenterInfo/tA2FvR')
time.sleep(2)
New_Edit(driver).write_form()
'''
