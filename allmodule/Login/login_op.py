from GLOBAL_USABLE import *
from allmodule.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from allmodule.Login.login_page import *
import allure


class Login(BasePage):
    """
    登录元素操作方法
    """
    # 打开网址
    @allure.step('打开网址')
    def open_url(self):
        return self.open(LOGIN_URL)

    # 输入账号
    @allure.step(f"输入账号：{USERNAME}")
    def username_input(self):
        return self.locator_with_wait(*username_input).send_keys(USERNAME)

    # 输入密码
    @allure.step(f"输入密码:{PASSWD}")
    def passwd_input(self):
        return self.locator_with_wait(*password_input).send_keys(PASSWD)

    # 点击登录按钮
    @allure.step("点击登录按钮")
    def login_btn(self):
        return self.locator_with_wait(*login_btn).click()

    # 进入MA工作台
    @allure.step("进入MA工作台")
    def play_open_ma(self):
        self.move_to_ele(*open_MA)

    # def login(self):
    #     with allure.step("打开登录页面"):
    #         self.open_url()
    #     with allure.step("输入密码"):
    #         self.username_input()
    #     with allure.step("打开登录页面"):
    #     self.passwd_input()
    #     with allure.step("打开登录页面"):
    #     self.login_btn()
    #     self.wait.until(EC.text_to_be_present_in_element(("xpath", "//*[text() ='我的应用']"), "我的应用"))
    #     # 进入工作台
    #     with allure.step("打开登录页面"):
    #     self.play_open_ma()
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.wait.until(EC.title_is("工作台"))

        
def login(browser):
    Lg = Login(browser)
    # with allure.step("登录页面"):
    Lg.open_url()
    Lg.username_input()
    Lg.passwd_input()
    Lg.login_btn()
    Lg.wait.until(EC.text_to_be_present_in_element(("xpath", "//*[text() ='我的应用']"), "我的应用"))
    # 进入工作台
    Lg.play_open_ma()
    Lg.driver.switch_to.window(browser.window_handles[-1])
    Lg.wait.until(EC.title_is("工作台"))
