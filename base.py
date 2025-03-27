
# 字符串和字节流的区别 u/b 前缀
def string():
    name="niel聂龙"
    print("name is:", name, ", id is:", id(name))
    print("type of name is: {}, len: {}".format(type(name), len(name)))

    mb=name.encode("utf-8")
    print("mb is: {}, id is {}".format(mb, id(mb)))
    print("type of mb is: {}, len: {}".format(type(mb), len(mb)))
    print(mb.decode("utf-8"))

if __name__ == "__main__":
    string()