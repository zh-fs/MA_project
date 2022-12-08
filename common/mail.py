
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import os, yaml
# 根目录
# dir = os.path.realpath(os.getcwd())
# 文件路径
# from common.Logger import logger, path

path = os.path.split(os.path.realpath(os.getcwd()))[0]

class mail:
    """

    用来获取配置并发送邮件
    """
    def __init__(self):
        # 读取配置文件
        with open(file=path+'/lib/conf.yaml',encoding='utf-8',mode='r') as file:
            self.mail_info = yaml.load(file,Loader=yaml.FullLoader)['mail']
        # 服务器地址
        self.mail_info['serveraddr'] = self.mail_info['serveraddr']
        # 发件人
        self.mail_info['from'] = self.mail_info['username']
        # 接收者
        self.mail_info['to'] = self.mail_info['to']
        # 设置主题
        self.mail_info['subject'] = Header(self.mail_info['mail_subject'],'utf-8').encode()

    def send_mail(self):
        """

        发送邮件：
        创建连接对象
        创建邮件对象
        附件
        :return:
        """
        # 创建连接对象
        smtp = smtplib.SMTP_SSL(self.mail_info['serveraddr'])
        # 登录邮箱
        smtp.login(self.mail_info['username'], self.mail_info['password'])

        # 普通HTML邮件
        # msg = MIMEText(text, 'html', self.mail_info['mail_encoding'])

        # 创建邮件对象
        mailject = MIMEMultipart()
        mailject['from'] = self.mail_info['from']
        mailject['To'] = self.mail_info['to']
        mailject['subject'] = self.mail_info['subject']
        mailject.attach(MIMEText('这是测试文件','plain','utf-8'))
        # 附件
        att = MIMEText(open(path+'/lib/testfile/1.xlsx','rb').read(), 'base64','utf-8')
        att.add_header('Content-Disposition','attachment', filename='1.xlsx')
        mailject.attach(att)
        smtp.sendmail(self.mail_info['username'], self.mail_info['to'].split(','), mailject.as_string())
        smtp.quit()
        # try:
        #     smtp.sendmail(self.mail_info['username'],self.mail_info['to'].split(','),mailject.as_string())
        #     smtp.quit()
        #     # logger.debug('邮件发送成功')
        # except Exception as e:
        #     # logger.error("邮件发送失败")
        #     # logger.exception(e)
if __name__ == '__main__':
    zh = mail()
    zh.send_mail()

