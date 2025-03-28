from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

from route import get_waypoint_route
from mob import get_mob_location
from weather import get_current_weather

llm = ChatOllama(
    base_url="http://168.3.0.114:11434",
    model="qwen2.5:14b", 
    temperature=0.7,
    # format= "json",
).bind_tools([get_current_weather, get_mob_location, get_waypoint_route])

prompt = ChatPromptTemplate.from_messages(
    [
        #("system", "你很聪明，但是个小话痨"),
        ("human","{input}")
    ]
)

chain = prompt | llm

def pprint(data: str):
    import json
    json_object = json.load(data)
    formtted = json.dumps(json_object, indent=2)
    print(formtted)

if __name__ == "__main__" :
    import sys
    input = sys.argv[1]
    print('<< ' + input)
    ai_msg = chain.invoke(input)
    messages = [HumanMessage(input)]
    # print(ai_msg.tool_calls)
    messages.append(ai_msg)

    for tool_call in ai_msg.tool_calls:
        selected_tool = {
            "get_mob_location": get_mob_location,
            "get_current_weather":get_current_weather,
            "get_waypoint_route":get_waypoint_route
        }[tool_call["name"].lower()]
        tool_message = selected_tool.invoke(tool_call)
        messages.append(tool_message)

    result = llm.invoke(messages)
    print('>> ' + result.content)

