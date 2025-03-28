from langchain_core.tools import tool
from typing import Tuple

@tool
def get_waypoint_route(origin: str, destination:str,
    origin_longitude:float, origin_latitude:float,
    destination_longitude:float, destination_latitude: float
) -> Tuple[Tuple[float, float], ...]:
    '''获取或制定从出发地点到达目的地的航线

    Args:
        origin(str): 出发地点的名称
        destination(str): 出发地点的名称
        origin_longitude(float): 出发地点的经度" },
        origin_latitude(float):  出发地点的纬度" },
        destination_longitude(float): 目的地的经度" },
        destination_latitude(float):  目的地的经度" }
    '''
    return ((1,2), (2,3))
    pass
