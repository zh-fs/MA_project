from selenium.webdriver.common.by import By

"""
交互中心表单页面element
"""
# 判断是否到了活动列表页面
assert_cc = [[By.XPATH, "//*[@class='f20']"], "表单"]

# 新建交互中心表单
new_center_form = [By.XPATH, "//*[text()='新建表单']"]
CC_new_Form = [By.XPATH, "//*[@name=0 and @temptype=30]/i"]
CC_name = [By.XPATH, "//*[@id='formContentName']"]
save_Form = [By.XPATH, "//*[@class='btn-lg btn-blue saveFormContent']"]

# 创建好直播后下断言使用，注意能搜出多个元素,定位元素时[0]为第一个,
# locators()，为了方便显示等待元素，用一下的写法，顺便断言也有了
assert_cc_name = [[By.XPATH, "//*[@class='title']"], 0]
# 打开表单页
open_cc_form = [[By.XPATH, "//*[@class='link-blue f12']"], 0]
# 删除表单
del_cc_form = [By.XPATH, "//*[@data-original-title='删除']", 0]  # 点击删除图标
check_box = [By.XPATH, "//div[contains(@class,'icheckbox_square-blue')]"]  # 勾选删除复选框
del_cc_sure = [By.XPATH, "//*[@id='delBtn' and text()='删除']"]  # 点击确认删除
assert_del_cc = [[By.XPATH, "//em[@id='success-message']"], "删除成功！"]  # 删除断言
