import requests
import time
import json
from urllib import parse
from urllib3 import disable_warnings
from urllib.parse import urlparse


# 一个武理自动登录程序
class AutoLoginWLAN:
    def __init__(self):
        self.session = requests.session()

    def testConnection(self):
        # time.sleep(60) # 等待网卡就绪
        try:
            res = self.session.get("http://captive.apple.com", verify=False, headers={"connection": "close"},
                                   allow_redirects=True)
        except Exception as e:
            return False  # 没有链接wifi
        # print(res.url)
        if len(res.history) == 2:
            # print(res.url.strip("http://172.30.21.100/tpl/whut/login.html?").split("&"))
            self.result = res.history[1].headers["location"]
            urlparse(self.result)
            param = parse.parse_qs(parse.urlparse(self.result).query)
            self.nasid = param["nasId"]
            # ip = result["ip"]
            # switchip = result["switchip"]
            # nasId = result["nasId"]
            # mac = result["mac"]
            return False
        else:
            return True

    def get_connection_status(self):
        try:
            self.testConnection()
            res = self.session.get("http://172.30.21.100/api/account/status", params={
                "token": ""
            })
            res_text = res.json()
            status_code = res_text.get("code")
            if status_code == 1:
                print("设备不在线，尝试连接")
                return False
            elif status_code == 0:
                print("已经联网，退出")
                return True
        except Exception as e:
            print("未连接到学校wifi， 退出")
            return True  # 由于没有链接到学校wifi，不可能访问172.30.21.100，所以必将连接不上，直接返回成功连接

    def login(self):
        # self.session.get("http://172.30.21.100/api/r/14")
        headers = {
            "Host": "172.30.21.100",
            "Origin": "http://172.30.21.100",
            "Referer": "http://172.30.21.100/tpl/whut/login.html?nasId=14",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        # http://172.30.21.100/tpl/whut/login.html?apgroup=WHUT-WLAN-Dual-MM12&apname=JB-YQ-TSG-1F02-C&cmd=login&essid=WHUT-WLAN&ip=10.116.80.116&mac=50%3Ac2%3Ae8%3A77%3A41%3Ad7&nasId=1&switchip=172.30.14.106&url=https%3A%2F%2Fwenku.baidu.com%2Fview%2F95e88593a7e9856a561252d380eb6294dc8822dd.html
        data = {
            "username": "",  # 填入自己的上网账号
            "password": "",  # 填入自己的上网密码
            "nasId": self.nasid,  # 需要获取
            "userIpv4": "",  # 可以改成对应ip和mac，指定上网 self.result["ip"]
            "userMac": "",  # 50-C2-E8-77-41-D7 self.result["mac"]
            "captcha": "",  # 不想做验证码，因为自己也没遇到过几次
            "captchaId": "",
            "switchip": ""  # 更新以后必须填switch ip，否则登陆不了 self.result["switchip"] 好像可以乱填
        }
        res = self.session.post("http://172.30.21.100/api/account/login", data=data)
        data = json.loads(res.text)
        if data["code"] != 0:
            print("登陆失败")
            return False
        else:
            return True

    def logout(self):  # 写一个登出接口，方便调试
        self.session.get("http://172.30.21.100/api/account/logout", params={
            "token": ""
        })


if __name__ == "__main__":
    disable_warnings()
    loginProcess = AutoLoginWLAN()
    errorCount = 0
    # time.sleep(60) # 等待网卡就绪
    while True:
        if not loginProcess.get_connection_status():
            # loginProcess.login()
            if loginProcess.login():
                print("成功联网")
                break
            time.sleep(5)  # 五秒重复一次登录
            errorCount += 1
        else:
            break
        if errorCount > 50:  # 50次失败自动退出
            break
    # loginProcess.login()
    # loginProcess.logout()