from langchain_core.tools import tool

@tool
def get_mob_location(mob: str) -> (float, float):
    '''获取标记点的经纬度位置

    Args:
        mob(str): 需要获取经纬度的标记点名称，比如：本船、当前位置
    '''
    return (11.111, 2.222)
    pass

