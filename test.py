print("Hello world")
print("你好，")
# 字符串和字节流的区别 u/b 前缀
def string():
    name="niel聂龙"
    mb=name.encode("utf-8")
    print(mb)
    print("type: {}, len: {}".format(type(mb), len(mb)))
    print(mb.decode("utf-8"))

import time
def consumer():
    """消费者作为生成器"""    
    prod=[]
    while True:
        if(len(prod)==0):
            # 让出
            yield prod
        else:
            print("consumer:...")
            print("\t", end='')
            for n in prod:
                time.sleep(0.5)
                print(n, end=' ', flush=True)
            print()
            prod.clear()

def producer(c: consumer):
    """生产者作为普通函数"""
    n=0
    prod = next(c)
    while True:
        if(len(prod)>4):
            # 通知 consumer 消费并让出
            prod = next(c)
        else:
            print("producer: prepare {}".format(n))
            time.sleep(0.3)
            prod.append(n)          
            n+=1

c=consumer()
producer(c)

# Get 营销活动 by http/https GET/POST from 源达云
import requests

class Yxhd(object):
    host="http://yun.ydtg.com.cn"
    daohang="/ydhxgtest/YingXiaoHuoDong/GuangGaoWeiPC/DaoHang"

def test():
    urls=[]
    urls.append("http://non-exist.com")
    urls.append("http://www.baidu.com")
    urls.append("https://www.baidu.com")
    for url in urls:
        r1=requests.get(url)
        print("Request {}\n\t{}: {}".format(url, r1, r1.reason))

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

# subscribe 涨停炸板 by websocket/websockets
# grpc


