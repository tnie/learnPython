import requests
import json
from sensitive.config import Robot

def select():
    pass

def msg():
    """参考钉钉开发平台要求，格式化数据对象：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq/e9d991e2"""
    content={"content": "【最大值】来自 python 的测试消息"}  #dict
    msg={"msgtype": "text", "text":content}
    return msg

def send():
    url ="https://oapi.dingtalk.com/robot/send?access_token="
    url += Robot.token
    r1=requests.post(url, json=msg())
    print("Request {}\n\t{}: {}".format(url, r1, r1.reason))
    print("发送结果：{}，内容：".format(r1))
    print(r1.text)

if __name__ == "__main__":
    send()
