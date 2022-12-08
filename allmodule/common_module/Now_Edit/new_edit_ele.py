from selenium.webdriver.common.by import By
from common.random_number import *

"""
新编辑器元素
默认模板(一加二)
"""
# 目前表单只有姓名与手机号
random_data = [random_name(), random_number()]
# 编辑新编辑器需要显示等待新编辑器的元素出现
wait_new_edit_ele = [By.XPATH, "//*[@id='fakeLoader']"]
new_Form = [By.XPATH, "//*[@name=0 and @temptype=30]/i"]  # 选择表单空白模板
# 添加表单,注：默认模板加表单用第一个(有多个)
add_Form = [[By.XPATH, "//*/a[@class='add-content panel-opend-left-320']"], 0]
# print(*add_Form[0])
sel_Form = [By.XPATH, "//*[@class='nav-link']"]  # 选择表单类型为系统表单
Form = [By.XPATH, "//*[text() = '+添加表单']"]
# 获取表单id属性值，方便后续提交表单使用
Form_ele = [By.XPATH, "//*/app-content-body/div[@class='ng-star-inserted']"]
# 点击发布按钮
release_Form = [By.XPATH, "//*[@ngbtooltip='发布']"]

# 填写表单,只有输入框的话就是使用这个locator，
# 注意该定位有多个
write_Form = [By.XPATH, "//input"]
# 立即报名
apply_bnt = [By.XPATH, "//*[@class='text-ellipsis' and text()='立即报名']"]
# 报名成功断言
apply_assert = [[By.XPATH, "//*[@class='modal-title mix-mt-20']"], "报名成功"]