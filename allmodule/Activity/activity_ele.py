from selenium.webdriver.common.by import By


"""
活动列表页面操作元素
"""
# 判断是否到了活动列表页面
assert_ac = [[By.XPATH, "//*[@class='f18']"], "活动列表"]

# 点击活动链接打开活动报名页面
ac_link_click = [By.XPATH, "//*[@id='activitylist']/div[1]//span[@class='link']/a"]

# 删除活动按钮
ac_del = [By.XPATH, "//div[@id='activitylist']/div[1]//i[@class='iconfont delType']"]
ac_del_sure = [By.XPATH, "//*[@id='delBtn']"]  # 点击确认删除按钮
assert_del_ac = [By.XPATH, "//*[@id='activitylist']/div[1]//span[@class='act-tt']/a"]

"""
新建一个活动操作
"""
# 新建活动按钮
create_ac = [By.XPATH, "//*[@class='btn-lg btn-blue ActivityCreate']"]
# 新建活动输入数据
# 活动名称
ac_name = [By.XPATH, "//input[@id='activityName']"]
# 活动分类
ac_type_click = [By.XPATH, "//em[@id='activityTypeText']"]
ac_type_sel = [By.XPATH, "//ul[@id='activityTypeList']/li[2]"]  # 选择第一个类别
# 操控时间插件用id定位 js_time_ele()
ac_start_time = "activityStarDate"  # 开始时间
ac_end_time = "activityEndDate"  # 结束时间
# 确定创建按钮
ac_sure_bnt = [By.XPATH, "//a[@class='btn-lg btn-blue ml5 activityCreateSure']"]
# 创建取消按钮
ac_cancel_bnt = [By.XPATH], "//div[@class='new-modal-footer']/div[@class='pull-right']/a[@class='btn-lg btn-gray-line']"
# 创建表单按钮
ac_create_form = [By.XPATH, "//a[@class='btn-lg btn-blue px30' and @data-toggle='modal']"]
# 选择表单类型(老表单1，老表单2，新编辑器表单)
ac_old_form01_type = [By.XPATH, "//*[@class='act-form-creat-box'][1]//a[text()='立即使用']"]  # 老表单1
ac_old_form02_type = [By.XPATH, "//*[@class='act-form-creat-box'][2]//a[text()='立即使用']"]  # 老表单2
ac_new_form_type = [By.XPATH, "//a[@class='btn-lg btn-green px30 openPageCreate']"]  # 新编辑器表单



