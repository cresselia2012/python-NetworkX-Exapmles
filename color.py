import networkx as nx
import matplotlib.pyplot as plt

# 有向グラフを定義
G = nx.DiGraph()

# ノードを追加
G.add_nodes_from([
    (0, {"color" : "darkorange"}),
    (1, {"color" : "lightblue"}),
    (2, {"color" : "lightblue"}),
    (3, {"color" : "lightblue"}),
    (4, {"color" : "royalblue"}),
    (5, {"color" : "royalblue"}),
    (6, {"color" : "royalblue"}),
    (7, {"color" : "steelblue"}),
    (8, {"color" : "steelblue"}),
    (9, {"color" : "steelblue"})
    ])

# エッジの追加(方法1)
edges = [
    (0, 1, {"color" : "lightblue"}),
    (1, 2, {"color" : "lightblue"}),
    (2, 3, {"color" : "lightblue"}),
    (3, 0, {"color" : "lightblue"})
    ]
G.add_edges_from(edges)

# エッジの追加(方法2)
nx.add_path(G, [0,4,5,6,0], color="royalblue")
nx.add_path(G, [0,7,8,9,0], color="steelblue")

# ノードの色をセット
node_color = [node["color"] for node in G.nodes.values()]

# エッジの色をセット
edge_color = [edge["color"] for edge in G.edges.values()]

# グラフを出力
fig = plt.figure()
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos, edge_color=edge_color, node_color=node_color)
plt.axis("off")
fig.savefig("test.png")
