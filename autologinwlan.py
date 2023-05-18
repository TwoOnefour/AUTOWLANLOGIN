import requests
import time
import json
from urllib import parse
from urllib3 import disable_warnings

# 一个武理自动登录程序
class AutoLoginWLAN:
    def testConnection(self):
        # time.sleep(60) # 等待网卡就绪
        try:
            res = requests.get("https://www.baidu.com/?cmd=redirect&arubalp=12345",verify=False)
        except Exception as e:
            return False # 没有链接wifi
        # print(res.url)
        if "https://www.baidu.com/?cmd=redirect&arubalp=12345" != res.url:
            # print(res.url.strip("http://172.30.21.100/tpl/whut/login.html?").split("&"))
            self.result = parse.parse_qs(parse.urlparse(res.url).query)
            # ip = result["ip"]
            # switchip = result["switchip"]
            # nasId = result["nasId"]
            # mac = result["mac"]
            return False
        else:
            return True
    def login(self):
        headers = {
            "Host":"172.30.21.100",
            "Origin":"http://172.30.21.100",
            "Referer":"http://172.30.21.100/tpl/whut/login.html?nasId=14",
            "Content-Type":"application/x-www-form-urlencoded"
        }
        # http://172.30.21.100/tpl/whut/login.html?apgroup=WHUT-WLAN-Dual-MM12&apname=JB-YQ-TSG-1F02-C&cmd=login&essid=WHUT-WLAN&ip=10.116.80.116&mac=50%3Ac2%3Ae8%3A77%3A41%3Ad7&nasId=1&switchip=172.30.14.106&url=https%3A%2F%2Fwenku.baidu.com%2Fview%2F95e88593a7e9856a561252d380eb6294dc8822dd.html
        data = {
            "username":"", # 填入自己的上网账号
            "password":"", # 填入自己的上网密码
            "nasId":14,
            "userIpv4": self.result["ip"],  # 可以改成对应ip和mac，指定上网
            "userMac": self.result["mac"], # 50-C2-E8-77-41-D7 self.result["mac"]
            "captcha":"", # 不想做验证码，因为自己也没遇到过几次
            "captchaId":"",
            "switchip":self.result["switchip"] # 更新以后必须填switch ip，否则登陆不了
        }
        res = requests.post("http://172.30.21.100/api/account/login",data=data)
        data = json.loads(res.text)
        if data["code"] != 0:
            print("登陆失败")
if __name__ == "__main__":
    disable_warnings()
    loginProcess = AutoLoginWLAN()
    errorCount = 0
    # time.sleep(60) # 等待网卡就绪
    while True:
        if not loginProcess.testConnection():
            loginProcess.login()
            time.sleep(5) # 五秒重复一次登录
            errorCount += 1
        else:
            print("已经联网，退出")
            break
        if errorCount > 50: # 50次失败自动退出
            break
