import os
import pytest
import allure


def run():
    pytest.main(['-s', '--alluredir', './result', '--clean-alluredir'])
    # 生成外部链接，注意链接需要改成自己本地IP去打开
    # os.system('allure serve result')
    # 生成文件，然后在pycharm中打开
    os.system("allure generate ./result -o ./report/html --clean")


if __name__ == '__main__':
    run()
"./testcase/activity/test_activity.py"
'./testcase/contentCenter'
"./testcase/Webtv/test_webtv.py"
"./testcase/content/test_content.py"
