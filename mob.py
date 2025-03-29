from langchain_core.tools import tool

def dangm():
    import dmPython

    try:
        conn = dmPython.connect(user='SYSDBA', password='SYSDBA', server='localhost', port=5236)
        cursor = conn.cursor()
        print('python: conn success!')
        conn.close()
    except (dmPython.Error, Exception) as err:
        print(err)

def get_current_location() :
    import time
    offset = time.time() % 100 / 100
    return (119.119 + offset,38.38 + offset)

@tool
def get_mob_location(mob: str) -> tuple[float, float]:
    '''获取标记点的经纬度位置

    Args:
        mob(str): 需要获取经纬度的标记点名称，比如：本船、当前位置
    '''
    marknodes = {
        "塘沽港5号码头": (117.73,38.98),
        "大连港邮轮中心": (121.66,38.93),
        "长兴岛": (121.80,31.36),
        "当前位置": get_current_location(),
        "本船": get_current_location(),
    }
    return marknodes.get(mob)
    pass

if __name__ == "__main__":
    location = get_mob_location("当前位置")
    print(location)