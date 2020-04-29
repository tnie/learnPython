import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import json
import requests
import time

def login():
    url='https://cs-hxg-api.zslxt.com/api/hxg/pc/v1/login'
    data='username=ydhxgys124&password=250799&device_id=00-FF-3B-AB-2F-5F'
    r1=requests.post(url, data=data)
    print("Request {}\n\t{}: {}".format(url, r1, r1.reason))
    print("使用 POST 获取营销活动的导航页：{}，内容：".format(r1))
    print(r1.text)
    if (r1):
        result=json.loads(r1.text)
        if(result['code']==10000):  #登录成功
            data=result['data']
            return (data['token'], data['s_token'])

def sso():
    (token, s_token)=login()
    websocket.enableTrace(True)
    url='wss://hxg-9509.zslxt.com/tuisong?'
    paras='catid={}&s_token={}&token={}'
    websocket.WebSocketApp('')

def on_message(ws, message):
    print(ws)
    print('\t', end='')
    print(json.loads(message))

def on_error(ws, error):
    print(error)
    pass

def on_close(ws):
    print(ws)
    print('#### closed ###')

def subMsg(cmd, node):
    user={'groups': [{'group_id': node}]}
    msg={'cmd': cmd,'user':user, 'path':node}
    return msg

def unused_variable(var):
    pass

def insert(ws, node, content):
    '''Failed. How?'''
    msg={'cmd':33,"path":node}
    msg["json"]=json.dumps(msg)
    str=json.dumps(msg)
    print(str)
    ws.send(str)


def on_open(ws):
    def run():
        node='yuanda/node/zbjtest/hxgzbj/classes'
        unused_variable(node)
        non_exist='UserCenter/test/Power2/HuiXuanGuHuoDong/-1'
        msg=subMsg(7, non_exist)
        ws.send(json.dumps(msg))
        time.sleep(3)
        insert(ws, 'yuanda/node/'+non_exist, 'test from python')
        time.sleep(3)
        print('closing...')
        ws.close()

    thread.start_new_thread(run, ())

url='wss://yun.ydtg.com.cn?username=niel&password=123'
ws =websocket.WebSocketApp(url, on_message=on_message,
    on_close=on_close,
    on_error=on_error)
ws.on_open=on_open
ws.run_forever()        # 没有 ping-pong 会被服务端关闭哟
