import os

import pytest
from selenium import webdriver
import allure
from allmodule.Login.login_op import login

# 测试用例失败截图


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


# 浏览器预置fix
@pytest.fixture(scope="session")
def browser():
    # 01 用例前置操作
    global driver
    driver = webdriver.Chrome()
    # 窗口可视最大化，方便看结果
    # driver.maximize_window()
    # # 02 移动窗口
    driver.set_window_position(1900, -200)
    driver.set_window_size(1550, 1000)
    # driver.minimize_window()
    with allure.step("登录"):
        login(driver)
    # 03 用例执行，返回driver
    yield driver

    # 04 用例后置，关闭浏览器
    driver.quit()

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makerreport():
