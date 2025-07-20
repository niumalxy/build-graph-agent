from tools.graph import *
from langchain.agents import load_tools

tools = [build_graph]
args = [edge, node, graph]

tools2function = {}