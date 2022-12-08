import datetime
from time import sleep
import allure
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # 方便写，后续记得注掉
        # self.driver = webdriver.Chrome()

    # 用于‘等待中’
    def wait_ele_vanish(self, ele):
        # 等待元素的出现
        self.locator_with_wait(*ele)
        # 等待元素的消失
        self.wait.until_not(EC.visibility_of_element_located(ele))

    # 当前时间
    def current_time(self):
        date = datetime.datetime.now()
        return str(date)

    # 使用js修改时间插件属性，然后修改时间
    def js_time_ele(self, e_id=None, t=0):
        # jQuery，移除属性
        date_time = (datetime.datetime.now() + datetime.timedelta(days=t)).strftime("%Y-%m-%d %H:%M:%S")
        if e_id is None:
            return date_time
        else:
            self.locator_with_wait('id', e_id).click()
            js = f"document.getElementById('{e_id}').removeAttribute('readonly')"
            # js = "document.getElementById('c-date1').removeAttribute('readonly')" # 1.原生js，移除属性
            # 12# js = "$('input[id=c-date1]').removeAttr('readonly')" # 2.jQuery，移除属性
            # 13# js = "$('input[id=c-date1]').attr('readonly',false)" # 3.jQuery，设置为false
            # 14 js = "$('input[id=c-date1]').attr('readonly','')"# 4.jQuery，设置为空（同3）
            # 15driver.execute_script(js)
            self.driver.execute_script(js)
            self.locator_with_wait('id', e_id).clear()
            self.locator_with_wait('id', e_id).send_keys(date_time)

    # 打开浏览器网址
    def open(self, url):
        self.driver.get(url)
        self.wait.until(EC.url_contains(url))

        # 元素定位&元素显式等待
    def locator_with_wait(self, key, value):
        locator = (key, value)
        self.wait.until(EC.visibility_of_element_located(locator))

        ele = self.driver.find_element(*locator)
        # 将定位的元素框出来
        self.locator_station(ele)
        return ele

    # 当元素不在页面上时，但在DOM树里面有，滑动到元素所在的位置
    def locator_with_wait_roll(self, key, value):
        locator = (key, value)
        self.wait.until(EC.presence_of_element_located(locator))
        ele = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        # self.wait.until(EC.visibility_of_element_located(locator))
        # 将定位的元素框出来
        self.locator_station(ele)
        return ele

    # 元素不可见时，滚到页面找到元素
    def roll_locator_ele(self, *elements):
        ele = self.driver.find_element(*elements)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        return ele

    # 元素定位
    def locator(self, key, value):
        ele = self.driver.find_element(key, value)
        # 将定位的元素框出来
        self.locator_station(ele)
        return ele

    # 定位多个元素值
    def locators(self, key, value, idx=None):
        locator = (key, value)
        ele_wait = self.wait.until(EC.visibility_of_all_elements_located(locator))
        # print(ele_wait)
        if idx is None:
            elements = self.driver.find_elements(*locator)
            return elements
        else:
            element = self.driver.find_elements(*locator)[idx]
            self.locator_station(element)
        # print(elements)
        # 将定位的元素框出来
        # self.locator_station(locator)
            return element
        # else:
        #     elements = self.driver.find_elements(*locator)[idx]
        #     self.locator_station(elements)
        #     return elements

    # 定位元素所在的地方，方便确认位置
    # def locator_station(self, ele):
    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('style', arguments[1]);",
    #         ele,
    #         "border: 2px solid green"   # 边框绿色
    #     )

    def locator_station(self, ele):
        self.driver.execute_script(
            "arguments[0].%s.setProperty(arguments[1],arguments[2])" % "style",
            ele,
            "border",
            "2px solid green")

    """
    显示等待方法封装
    """
    def wait_ele_visible(self, key, value):
        ele = (key, value)
        return self.wait.until(EC.visibility_of_element_located(ele))

    def wait_ele_text(self, ele, text):
        # print(ele)
        return self.wait.until(EC.text_to_be_present_in_element(ele, text))

    # 获取页面title信息
    def get_title(self):
        return self.driver.title

    # 只用Xpath定位元素,获得文本信息
    def get_text(self, xpath):
        return self.locator('xpath', xpath).text

    # 双击鼠标左键
    def double_click(self, *element):
        return ActionChains(self.driver).double_click(self.locator(*element)).perform()

    # 鼠标移动（悬浮）到元素上并点击,
    def move_to_ele(self, *elements):
        ac = ActionChains(self.driver)
        action = ac.move_to_element(self.driver.find_element(*elements)).click().perform()
        return

    # 拖拽到某个元素上松开
    def drag_to_drop(self, source, target):
        return ActionChains(self.driver).drag_and_drop(source, target).perform()

    def to_frame(self, value):
        return self.driver.switch_to.frame(value)

    # 退出frame，回到主页面
    def to_default_content(self):
        return self.driver.switch_to.default_content()

    # frame返回到上一级
    def to_parent_frame(self):
        return self.driver.switch_to.parent_frame()

    # 返回所有窗口的句柄
    def window_handles(self):
        return self.driver.window_handles

    # 当前的窗口句柄
    def current_window(self):
        return self.driver.current_window_handle

    # 切换窗口
    def switch_window(self, handle):
        return self.driver.switch_to.window(handle)

    # 切换到新开窗口
    # def current_to_next(self):
    #     current = self.current_window()
    #     all_handles = self.window_handles()
    #     for handle in all_handles:
    #         if handle != current:
    #
    #             return self.switch_window(handle)

    # 跳转到最后一个窗口
    def switch_end_hand(self):
        all_handles = self.window_handles()
        self.driver.switch_to.window(all_handles[-1])




    # 警告框处理
