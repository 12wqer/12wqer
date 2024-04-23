import pandas as pd
import numpy as np
import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/GREESHMA/Downloads/SMA Practicals/top_insta_influencers_data.csv")

G=nx.from_pandas_edgelist(data,'influence_score', 'avg_likes')

nodes=G.nodes()
print("\nThe nodes are: ",nodes)

edges=G.edges()
print("\nThe edges are:",edges)

degree_centrality = nx.degree_centrality(G)
print("\nDegree Centrality:", nx.degree_centrality(G))

betweenness_centrality = nx.betweenness_centrality(G)
print("\nBetweenness Centrality:", nx.betweenness_centrality(G))

edge_centrality = nx.edge_betweenness_centrality(G)
print("\nEdge Betweenness Centrality:", nx.edge_betweenness_centrality(G))

eigenvector_centrality = nx.eigenvector_centrality(G)
print("\nEigenvector Centrality:", nx.eigenvector_centrality(G))

bridges = list(nx.bridges(G))
print("\nBridges in the network:", bridges)

plt.figure(figsize=(20, 8))
nx.draw(G, with_labels=True, node_size=500, node_color='pink', font_size=8, font_weight='bold')
plt.title('Facebook Network Graph')
plt.show()