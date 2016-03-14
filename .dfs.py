import matplotlib.pyplot as plt
import networkx as nx
G =nx.Graph()
Ostov = nx.Graph()
G.add_edge(1,2)
G.add_edge(1,8)
G.add_edge(2,3)
G.add_edge(2,8)
G.add_edge(3,4)
G.add_edge(3,8)
G.add_edge(4,7)
G.add_edge(4,9)
G.add_edge(5,6)
G.add_edge(5,7)
G.add_edge(7,8)

def call_friend(G, start, called):
    called.add(start)
    for neighbour in G[start]:
        if neighbour not in called:
            Ostov.add_edge(start,neighbour)
            call_friend(G, neighbour, called)
called = set()
call_friend(G,1,called)
nx.draw_spectral(Ostov)
plt.show()
