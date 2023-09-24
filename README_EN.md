# What is this

A python script automatically auth via portal in WHUT.

To prevent complex and repeatedly enter the username and password to auth Wi-Fi, the script is birth.

It will function when you boot and automatically connect to the correct Wi-Fi, such as WHUT-WLAN, WHUT-WLAN6, etc.

# How to use
## Select "connect automatically" option while connecting
![image](https://user-images.githubusercontent.com/77989499/224923133-9a068917-48b9-4ba3-b363-eecdf4c8b521.png)

## Edit the python file 
You should edit the username and password before you use it.The script don't collect any private message, don't worry.

![image](https://user-images.githubusercontent.com/77989499/224918771-e064b9a2-f772-49e2-843b-bb077b182afb.png)

Then you can run it by directly using python command like 

<code>python ./autologinwlan.py</code>.

## Use it by running exe
Pyinstaller is an another optional consideration.

<code>pyinstaller ./autologinwlan.py -F -w</code>.

If it doesn't works properly, plz install pyinstaller by

<code>pip install pyinstaller </code>.

By generating an execution file, you can put it in "startup" folder by pressing WIN+R, entering "shell:startup" and dragging it into the folder.
![image](https://user-images.githubusercontent.com/77989499/224920640-6f6dde7e-5750-42b4-a3a0-763fd33b0f3c.png)

![image](https://user-images.githubusercontent.com/77989499/224920678-7ea0e76b-0b6f-4327-b210-139be93ac36c.png)

This is my [blog](https://www.pursuecode.cn "blog") link.

If anything work wrongly, plz open an issue.

Enjoy it :).
