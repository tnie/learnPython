
import time
def consumer():
    """消费者作为生成器"""
    while True:
        prod=yield
        print("consumer:... from {}".format(id(prod)))
        print("\t", end='')
        for n in prod:
            time.sleep(0.5)
            print(n, end=' ', flush=True)
        print()
        prod.clear()

def producer(c: consumer):
    """生产者作为普通函数"""
    n=0
    prod = []
    c.send(None)
    while True:
        # 通知 consumer 消费并让出
        print("use prod@{}".format(id(prod)))
        for i in range(5):
            print("producer: prepare {}".format(n))
            time.sleep(0.3)
            prod.append(n)
            n+=1
        c.send(prod)    # next(c)
        if(n>8):
            c.close()   # 如果不关闭，则 45-46 行就不会抛出异常
            break

c=consumer()
producer(c)
try:
    c.send([])
    c.send(list(range(100,105)))
except StopIteration as e:
    print("StopIteration: {}".format(e))
