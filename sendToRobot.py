import requests
import json


def select():
    pass

def msg():
    """参考钉钉开发平台要求，格式化数据对象：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq/e9d991e2"""
    content={}  #dict
    content["content"]="【最大值】来自 python 的测试消息"
    msg={}
    msg["msgtype"]="text"
    msg["text"]=content
    return msg

def data():
    """对象转换为 json 字符串"""
    return json.dumps(msg())

def send():
    url ="https://oapi.dingtalk.com/robot/send?access_token="
    token="355e025300fb8b07fe1f471e2943ee697e6d81f221a93faaa20ce7c7ccf9686c"
    url += token
    # r1=requests.post(url, data(), headers={"Content-Type: application/json"})
    r1=requests.post(url, data=data(), headers={"Content-Type": "application/json;charset=utf-8"})
    # r1=requests.post(url, json=msg())
    print("Request {}\n\t{}: {}".format(url, r1, r1.reason))
    print("发送结果：{}，内容：".format(r1))
    print(r1.text)

    pass

send()
