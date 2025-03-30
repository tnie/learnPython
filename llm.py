from route import get_waypoint_route
from mob import get_mob_location
from weather import get_current_weather

def transcribe(audio:str = "./speech/1743306875018.mp3") -> str:
    import whisper
    model = whisper.load_model("small")
    result = model.transcribe(audio)
    # print(result)
    return result["text"]

def chain():
    import os
    if os.system("ping 192.168.50.1 -n 2"):
        from langchain_ollama import ChatOllama
        print("using ChatOllama...")
        return ChatOllama(
            base_url="http://168.3.0.114:11434",
            model="qwen2.5:14b", 
            temperature=0.7,
            # format= "json",
        ).bind_tools([get_current_weather, get_mob_location, get_waypoint_route])
    else:
        from langchain_deepseek import ChatDeepSeek
        print("using ChatDeepSeek...")
        return ChatDeepSeek(
            model="deepseek-chat",
            temperature=0,
            # max_tokens=None,
            timeout=None,
        ).bind_tools([get_current_weather, get_mob_location, get_waypoint_route])

def tellme(query: str):
    print('<< ' + query)
    if(not query.strip()):
        return print("do nothing.")
    llm = chain()
    from langchain_core.messages import (HumanMessage, SystemMessage)
    messages = [
        SystemMessage("""制定航线时如果没能获取到具体的经纬度，请使用常见的坐标进行路线规划。"
        "如果用户没有提供出发地点，请使用本船的当前位置"""),
        HumanMessage(query)
    ]
    for multi in range(5):
        ai_msg = llm.invoke(messages)
        if(not ai_msg.tool_calls): 
            print('>> ' + ai_msg.content)
            break
        cnt = len(ai_msg.tool_calls)
        print(F"LLM 第{multi+1}次答复，指示调用{cnt}次工具", ai_msg.tool_calls)
        messages.append(ai_msg)

        for tool_call in ai_msg.tool_calls:
            selected_tool = {
                "get_mob_location": get_mob_location,
                "get_current_weather":get_current_weather,
                "get_waypoint_route":get_waypoint_route
            }[tool_call["name"].lower()]
            tool_message = selected_tool.invoke(tool_call)
            # print(tool_message)
            messages.append(tool_message)
        
        # print(messages)

if __name__ == "__main__" :
    import sys
    query = "".join(sys.argv[1:])
    if(query.endswith(".mp3")):
        query = transcribe(query)
    tellme(query)
    
    [
        "我想去大连",
        "制作去塘沽港5号码头的航线",
        "怎么从长兴岛去大连港邮轮中心",
        "怎么从东经111.11°北纬33°33.33′去大连港邮轮中心",
        "制作一条从大连港邮轮中心去东经111.11°北纬33°33.33′的航线",
        "怎么从东经111.11°北纬33°33.33′去东经112.22°北纬34°33.33′",
    ]
    