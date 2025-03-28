from langchain_core.tools import tool

@tool
def get_current_weather(location: str):
    '''获取指定地点当天的天气

    Args:
        location(str): 需要获取天气的地点，比如：北京
    '''
    pass
