import sys, os
sys.path.append(os.path.dirname(os.path.abspath("__file__")).split('chat')[0])
from conf.conf import conf
from openai import OpenAI
from tools.factory import *
from langchain_openai import ChatOpenAI, OpenAI
import json
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from tools.prompt import *
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import load_tools

os.environ["OPENAI_API_KEY"] = conf["chat_model_api_key"]
os.environ["OPENAI_API_BASE"] = conf["chat_model_url"]
print(conf["chat_model_url"])
chat_client = ChatOpenAI(
    api_key=conf["chat_model_api_key"],  # 如果您没有配置环境变量，请在此处用您的API Key进行替换
    base_url=conf["chat_model_url"], # 百炼服务的base_url
    model=conf['chat_model_name']
)
#将工具绑定至模型中
Tools = load_tools([], llm=chat_client)
Tools += tools
agent = initialize_agent(Tools, chat_client, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# chain = chat_client.bind_tools(tools)
# chain = chat_client | PydanticToolsParser(tools=args)
if __name__ == "__main__":
    if not os.path.exists("output"):
        os.mkdir("output")
    while True:
        user = input("请输入流程描述：")
        query = START.replace("{user_input}", user)
        print(agent.run(query))