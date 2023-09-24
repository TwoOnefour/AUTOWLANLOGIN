# 这是什么
这是一个自动登录武汉理工wifi的小脚本，为了避免反复登录wifi，我写了这个程序

[ENG](https://github.com/Taxzer/AUTOWLANLOGIN/blob/main/README_EN.md "ENG") | 中文

# 该怎么用呢

## 连接wifi的时候使用自动连接
![image](https://user-images.githubusercontent.com/77989499/224922959-486955ed-ce76-471e-aa76-6b6d9a128877.png)

## 填入上网账号密码
首先你得编辑python文件，把你的上网账号和密码填入data，如图
![image](https://user-images.githubusercontent.com/77989499/224918771-e064b9a2-f772-49e2-843b-bb077b182afb.png)

然后你可以直接在终端中运行它

<code>python ./autologinwlan.py</code>.

## 使用exe自动化
使用pyinstaller打包生成exe文件

<code>pyinstaller ./autologinwlan.py -F -w</code>.

然后把文件放入开机启动项文件夹，这样每次你到了学校wifi的地方，开机自动连接上wifi，程序会自动帮你登录
![image](https://user-images.githubusercontent.com/77989499/224920640-6f6dde7e-5750-42b4-a3a0-763fd33b0f3c.png)

![image](https://user-images.githubusercontent.com/77989499/224920678-7ea0e76b-0b6f-4327-b210-139be93ac36c.png)

如果出现报错，多半可能你电脑环境没有pyinstaller，直接下一个就好了

<code>pip install pyinstaller </code>.

如果下载速度太慢，请按ctrl+c取消操作，然后使用清华等镜像源

<code>pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple </code>.

如果有什么不正确的地方，请发issue，我会尽量帮助你

Enjoy
