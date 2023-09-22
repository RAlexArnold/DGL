# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:51:33 2023

@author: Alex
"""

import networkx as nx
import dgl
import matplotlib.pyplot as plt

g_nx = nx.petersen_graph()
g_dgl = dgl.DGLGraph(g_nx)

plt.figure(1)
plt.subplot(121)
nx.draw(g_nx, with_labels=True)
plt.subplot(122)
nx.draw(g_dgl.to_networkx(), with_labels=True)

g_g = dgl.from_networkx(g_nx)

plt.figure(2)
plt.subplot(121)
nx.draw(g_nx, with_labels=True)
plt.subplot(122)
nx.draw(g_g.to_networkx(), with_labels=True)

plt.show()