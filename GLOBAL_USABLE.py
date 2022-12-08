
# 大写为全局变量
# 测试封面图片路径
IMAGE = r"D:\MA_project\img\testimage.png"
# 定位加载中元素
LOADING_ELE = ["xpath", "//*[@id='ma-Updata']"]
# ACCESSORY =
"""
登录账号密码
"""
# 测试环境登录url
LOGIN_URL = "https://cas.focussend.com/user/login"
# 测试环境登录账号
USERNAME = '18874080626@139.com'
# 测试环境登录密码
PASSWD = 'abc123'
MA_host = 'https://wx.vipmaillist.com'


# 正式环境登录url
# LOGIN_URL = "https://main.focussend.com/user/login"
# # 正式环境登录账号
# USERNAME = 'demo01@focussend.com'
# # 正式环境登录密码
# PASSWD = 'Fsend08'
# MA_host = 'https://wx.focussend.com/'
"""
MA域名
正式环境：'https://wx.focussend.com/'
测试环境：'https://wx.vipmaillist.com'
"""


# 内容页面URL
CONTENT_URL = MA_host + "/contentMarketing/toContentList"
# 直播页面URL
WEBTV_URL = MA_host + "/webtvInfo/toWebtvInfo"
# 活动页面URl
ACTIVITY_URL = MA_host + "/activity/activityManage"
# 交互中心表单页面URl
CENTER_FORM_URL = MA_host + "/contentCenter/toContentFormList?type=20"


