from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b")
llm.invoke("The meaning of life is")