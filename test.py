print("Hello world")
print("你好，")
# 字符串和字节流的区别 u/b 前缀
def string():
    name="niel聂龙"
    mb=name.encode("utf-8")
    print(mb)
    print("type: {}, len: {}".format(type(mb), len(mb)))
    print(mb.decode("utf-8"))

# Get 营销活动 by http/https GET/POST from 源达云
import requests

class Yxhd(object):
    host="http://yun.ydtg.com.cn"
    daohang="/ydhxgtest/YingXiaoHuoDong/GuangGaoWeiPC/DaoHang"

def test():
    r1=requests.get("http://non-exist.com")
    print("{}: {}".format( r1, r1.reason))
    r1=requests.get("http://www.baidu.com")
    print("{}: {}".format( r1, r1.reason))
    r1=requests.get("https://www.baidu.com")
    print("{}: {}".format( r1, r1.reason))

def daohang():
    node="/node/get?path="
    r1=requests.get(Yxhd.host+node+Yxhd.daohang)
    print("获取营销活动的导航页：{}，内容：".format(r1))
    print(r1.text)   # 通信返回 200，内容是 404 —— 无力吐槽

import json

def daohang2():
    data={}
    data["api"]="/get"
    data["nodePath"]=Yxhd.daohang
    url = Yxhd.host + "/node/sdkapi?token=niel"
    jdata=json.dumps(data)
    print("jdata's type: {}".format(type(jdata)))
    r1 = requests.post(url, jdata)
    print("使用 POST 获取营销活动的导航页：{}，内容：".format(r1))
    print(r1.text) 
    print("{}: {}\n".format(type(r1.request.body), r1.request.body))

    msg =json.loads(r1.text)
    nc=msg["nodeContent"]
    print("去除冗余的状态信息：\n"+nc)

def fail():
    data={}
    data["api"]="/get"
    data["nodePath"]=Yxhd.daohang
    url = Yxhd.host + "/node/sdkapi?token=niel"

    print(json.dumps(data))
    r1 = requests.post(url, None, json.dumps(data))
    print("使用 POST 获取营销活动的导航页：{}，内容：".format(r1))
    print(r1.text) 
    print(r1.request.body)

daohang()
daohang2()
# subscribe 涨停炸板 by websocket/websockets
# grpc


