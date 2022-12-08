from selenium.webdriver.common.by import By


"""
直播操作按钮：
    ‘分享、设置表单、链接、渠道码、统计、编辑、删除、共享、分配记录’
"""
# 判断是否到了直播页面
assert_tv = [[By.XPATH, "//*[@class='f18']"], "我的直播"]
# print(assert_tv[0], assert_tv[1])

# shareTV = [By.XPATH, "@data-original-title='分享']"]
# 设置表单,注意能搜出多个元素,定位元素时[0]为第一个，locators()
setTVForm = [By.XPATH, "//*[@data-original-title='设置表单']", 0]  # 设置表单按钮
setTVForm_content = [By.XPATH, "//*[@class='btn-lg btn-blue px30' and @data-toggle='modal']"]  # 表单内容
new_edit = [By.XPATH, "//*[@class='btn-lg btn-green px30 openPageCreate']"]  # 选择新编辑器

old_edit = [By.XPATH, "//*[@class='btn-lg btn-blue px30' and text()='立即使用']"]  # 选择老表单

# 设置完表单后，获取表单并打开,下面这个是获取url的定位，属性value的值
gina_tv_url = [By.XPATH, "//*[@id='txtUrl']"]

# 删除直播，注意能搜出多个元素,定位元素时[0]为第一个
delTV = [By.XPATH, "//*[@data-original-title='删除']"]  # 点击删除
del_bnt = [By.XPATH, "//*[text()='删除']"]  # 确认删除
assert_del_tv = [[By.XPATH, "//em[@id='success-message']"], "删除成功"]

# print(*(assert_del_tv[0]))

# 创建好直播后下断言使用，注意能搜出多个元素,定位元素时[0]为第一个,
# locators()，为了方便显示等待元素，用一下的写法，顺便断言也有了
assert_newtv = [[By.XPATH, "//*/a[@class='link-auto']"], 0]


# 新建直播按钮
new_WebTv = [By.XPATH, "//*[text()='新建直播']"]
"""
创建直播必填的,也可以在修改直播中使用
"""
# 直播名字
TvName = [By.XPATH, "//input[@id='txtName']"]
# 直播类型选择，在选择直播类型时需要先把下拉框展开出来
TvType = [By.XPATH, "//*[@id='tvType']"]
# 直播类型按照文本值来选择(10:其他，20：微吼直播，30：盟主直播，40：展视互动直播，:60：保利威)
# 为了方便，这里直接选择了‘其他’类型的
S_TvType = [By.XPATH, "//div/ul[@role='menu']/li/a[text()='其他']"]
# 选择‘其他’内型后需要输入观看地址,为了方便默认使用了百度网址（可以改）
txtTvUrl = [By.XPATH, "//input[@id='txtTvUrl']"]
txt_url = "https://www.baidu.com"
# 操控时间插件用id定位 js_time_ele()
create_time = 'txtStartTime'
end_time = "txtEndTime"
# 上传封面图片,这里用的是input标签，可以直接输入文件路径
upload_tv_img = [By.XPATH, "//*/form[@id='cover_form']/input"]
# 内容简介页按钮
intro_btn = [By.XPATH, "//*/span/a[text()='设置详情页']"]
# 简介页内容,输入内容需要跳转到iframe，这里用id跳转到iframe窗口
# intro_iframe_id = ["ueditor_0"]
intro_input = [By.XPATH, "//*/iframe[@id='ueditor_0']"]
save_intro = [By.XPATH, "//*[text()='保存设置']"]
# 发布直播
save_webtv = [By.XPATH, "//*[@id='saveWebtv']"]
# 点击弹框里的完成
finish_btn = [By.LINK_TEXT, "完成"]





