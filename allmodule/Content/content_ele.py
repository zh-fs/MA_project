from selenium.webdriver.common.by import By
"""
我的内容页面element
"""

# 判断是否到了活动列表页面
assert_ct = [[By.XPATH, "//*[@class='f18']"], "我的内容"]

# 上传内容按钮
push_ct = [By.XPATH, "//*[@class='btn-lg btn-blue']"]
# 新建内容设置页面-内容名称
ct_name = [By.XPATH, "//*[@id='txtName']"]
# 内容标题
ct_title = [By.XPATH, "//*[@id='txtTitle']"]
# 上传封面图片//*/form[@id='cover_form']/input
upload_ct_cover = [By.XPATH, "//*/input[@id='cover_pic']"]
# 内容简介页按钮
ct_intro_btn = [By.XPATH, "//a[text()='设置内容页面']"]
# 内容简介页面输入框
ct_intro_input = [By.XPATH, "//*/iframe[@id='ueditor_0']"]
# 内容简介页保存按钮
ct_save_intro = [By.XPATH, "//*[text()='保存设置']"]
# 内容资料附件
update_ct_accessory = [By.XPATH, "//form[@id='content_form']/input"]
# 是否允许PC端下载资料、
yes_not_download = [By.XPATH, "//*[@id='pcDownload']"]
# 发布内容
release_ct = [By.XPATH, "//*[@id='saveContent']"]
# 确认发布
sure_release = [By.XPATH, "//a[@class='btnblock-lg btn-blue ml5 mr25' and @href]"]
# 判断内容是否新建成功
assert_ct_create = [By.XPATH, "//a[@target='_blank' and @href and @title]"]




