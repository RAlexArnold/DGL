# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:41:06 2023

@author: Alex
"""

import os

os.environ["DGLBACKEND"] = "pytorch"
import dgl
import numpy as np
import torch
import networkx as nx
import matplotlib.pyplot as plt

'''
DGL represents a directed graph as a DGLGraph object. You can construct a graph by specifying the number of nodes in the graph as well as the list of source and destination nodes. Nodes in the graph have consecutive IDs starting from 0.

For instance, the following code constructs a directed star graph with 5 leaves. The center node’s ID is 0. The edges go from the center node to the leaves.

The nodes and edges are defined below by using the first list to represent the center node, and the second list to represent each node that is linked to the center node
'''

g = dgl.graph(([0, 0, 0, 0, 0], [1, 2, 3, 4, 5]), num_nodes=6)
# Equivalently, PyTorch LongTensors also work.
g = dgl.graph(
    (torch.LongTensor([0, 0, 0, 0, 0]), torch.LongTensor([1, 2, 3, 4, 5])),
    num_nodes=6,
)

# You can omit the number of nodes argument if you can tell the number of nodes from the edge list alone.
g = dgl.graph(([0, 0, 0, 0, 0], [1, 2, 3, 4, 5]))

# Print the source and destination nodes of every edge.
print(g.edges())

plt.figure(1)
plt.subplot(111)
nx.draw(g.to_networkx(), with_labels=True)


'''
The dgl.DGLGraph(...) and dgl.graph(...) functions in DGL serve slightly different purposes and are used in different contexts:

dgl.DGLGraph is a class constructor for creating a DGL graph object.
It is typically used when you want to create and manipulate a graph explicitly as a DGL graph object.
You can use it to create both homogeneous and heterogeneous graphs.
It allows fine-grained control over graph creation and manipulation, including adding nodes, edges, and specifying edge types for heterogeneous graphs.

dgl.graph is a function for creating a DGL graph from existing data structures, such as NumPy arrays or SciPy sparse matrices.
It is commonly used when you have existing data in the form of arrays or matrices and want to convert it into a DGL graph.
While it is primarily used for creating homogeneous graphs, you can use it for creating simple graphs without specifying edge types for heterogeneous graphs.
'''


# Alternatively, you can set the number of nodes, and add edges individually using DGLGraph()
g_dgl = dgl.DGLGraph()
g_dgl.add_nodes(6)
# a couple edges one-by-one
for i in range(1, 6):
    g_dgl.add_edges(0, i)
    
plt.figure(2)
plt.subplot(111)
nx.draw(g_dgl.to_networkx(), with_labels=True)

