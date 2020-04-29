
# 字符串和字节流的区别 u/b 前缀
def string():
    name="niel聂龙"
    print("len is:", len(name), ", id is:", id(name))
    mb=name.encode("utf-8")
    print("mb is: {}, id is {}\n type of mb is: {}, len: {}".format(mb, id(mb), type(mb), len(mb)))
    print(mb.decode("utf-8"))


if __name__ == "__main__":
    string()