import graphviz as gv
import subprocess, os

cur_path = os.path.abspath(".")
dot = gv.Digraph(comment="5")
dot.node("啊啊", "啊啊啊啊", fontname="Microsoft Yahei")
dot.save('result.dot', "output")
with open("output/result.dot",encoding='utf-8') as f:
    dot_graph = f.read()
graph=gv.Source(dot_graph.replace("helvetica","SimSun"))
graph.view()

# print(os.path.join(cur_path,r'output\result.dot'))
# cmd = [r'D:\Graphviz\bin\dot.exe', '-Tpng', os.path.join(cur_path, r'output\result.dot'), '-o', os.path.join(cur_path, r'output\result.png')]
# result = subprocess.run(cmd)
