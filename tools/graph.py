import graphviz as gv
from pydantic import BaseModel, Field
from langchain_core.tools import tool, BaseTool
from typing import Optional, Type
from langchain_core.callbacks import CallbackManagerForToolRun, AsyncCallbackManagerForToolRun
import subprocess, os
cur_path = os.path.abspath(".")
cmd = [r'D:\Graphviz\bin\dot.exe', '-Tpng', os.path.join(cur_path, r'output\round-table.gv'), '-o', os.path.join(cur_path, r'output\result.png')]

result = subprocess.run(cmd)

class edge(BaseModel):
    description: str = Field(default="", description="该边的名称")  
    subnode: str = Field(description="该边连接的子节点的名称")

class node(BaseModel):
    name: str = Field(description="节点名称")
    edges: list[edge] = Field(default=[], description="连接该节点的所有边")

class graph(BaseModel):
    title: str = Field(default="", description="流程图名称")
    StartNode: node = Field(description="开始的节点")
    NodeList: list[node] = Field(description="所有的节点列表")

# class BuildGraph(BaseTool):
#     name = "BuildGraph"
#     description = 
#     args_schema: Type[BaseModel] = graph
#     return_direct: bool = True

#     def _run(
#         self,
#         items,
#         run_manager: Optional[CallbackManagerForToolRun] = None
#     ) -> int:
#         """执行工具"""
#         build_graph(items)
#         return "流程图构建完成"

#     async def _arun(
#         self,
#         a: int,
#         b: int,
#         run_manager: Optional[AsyncCallbackManagerForToolRun] = None
#     ) -> int:
#         """异步执行工具"""
#         return self._run(a, b, run_manager=run_manager)

@tool("build_graph", return_direct=True, args_schema=graph)
def build_graph(**kwargs):
    """根据用户所给的流程绘制流程图"""
    print("build graph...")
    args = graph.model_validate(kwargs)
    dot = gv.Digraph(comment=args.title)
    node_name = 'A'
    queue = [(node_name, args.StartNode)]
    while queue:
        #增加节点
        node = queue.pop(0)
        dot.node(node[0], node[1].name, fontname="Microsoft Yahei")
        for e in node[1].edges:
            for n in args.NodeList:
                if e.subnode == n.name:
                    queue.append((node_name := chr(ord(node_name) + 1), n))
                    dot.edge(node[0], node_name, label=e.description, fontname="Microsoft Yahei")
                    break
    dot.save('round-table.gv', 'D:/tools_dev/流程图/output/')
    result = subprocess.run(cmd)
    return "绘制成功"





