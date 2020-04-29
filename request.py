
# Get 营销活动 by http/https GET/POST from 源达云
import requests
import json

def test():
    urls=("http://non-exist.com", "http://www.baidu.com" ,"https://www.baidu.com")
    for url in urls:
        r1=requests.get(url)
        print("Request {}\n\t{}: {}".format(url, r1, r1.reason))

class Yxhd():
    host="http://yun.ydtg.com.cn"
    daohang="/ydhxgtest/YingXiaoHuoDong/GuangGaoWeiPC/DaoHang"

def daohang():
    node="/node/get?path="
    r1=requests.get(Yxhd.host+node+Yxhd.daohang)
    print("获取营销活动的导航页：{}，内容：".format(r1))
    print(r1.text)   # 通信返回 200，内容是 404 —— 无力吐槽

def daohang2():
    data={"api":"/get", "nodePath": Yxhd.daohang}
    url = Yxhd.host + "/node/sdkapi?token=niel"
    r1 = requests.post(url, json=data)
    # r1 = requests.post(url, data=json.dumps(data))  # ok
    # r1 = requests.post(url, data=data)              # fail
    # r1 = requests.post(url, json=json.dumps(data))  # fail
    print("使用 POST 获取营销活动的导航页：{}，内容：".format(r1))
    print(r1.text)
    print("{}: {}\n".format(type(r1.request.body), r1.request.body))

    msg =json.loads(r1.text)
    nc=msg["nodeContent"]
    print("去除冗余的状态信息：\n"+nc)

if __name__ == "__main__":
    daohang2()


# subscribe 涨停炸板 by websocket/websockets
# grpc
