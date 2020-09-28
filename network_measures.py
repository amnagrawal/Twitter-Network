import networkx as nx
from matplotlib import pyplot as plt


def degree_distribution(G, title=""):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    plt.hist(degree_sequence, rwidth=0.8)
    plt.title(title)
    plt.ylabel("Count")
    plt.xlabel("Degree")
    plt.show()


def draw_graph(G, title=""):
    plt.figure(figsize=(10, 10))
    node_size = [0.7*G.degree(v) for v in G]
    node_color = [G.degree(v) for v in G]
    nx.draw_networkx(G, edge_color="grey", with_labels=False, node_color=node_color,
                     alpha=0.7, cmap=plt.get_cmap('winter'), node_size=node_size,
                     width=0.2)

    plt.axis('off')
    plt.title(title)
    plt.show()


def get_top_keys(dictionary, top):
    items = list(dictionary.items())
    items.sort(reverse=True, key=lambda x: x[1])
    return list(zip(map(lambda x: x[0], items[:top]),
                    map(lambda x: round(x[1], 4), items[:top])))


def centrality_measures(g):
    bet_cen = nx.betweenness_centrality(g)
    clo_cen = nx.closeness_centrality(g)
    eig_cen = nx.eigenvector_centrality(g)
    pagerank_cen = nx.pagerank(g)
    reciprocity_cen = nx.reciprocity(g)

    top_bet_cen = get_top_keys(bet_cen, 10)
    top_clo_cen = get_top_keys(clo_cen, 10)
    top_eig_cen = get_top_keys(eig_cen, 10)
    top_pagerank_cen = get_top_keys(pagerank_cen, 10)

    print(f"Top 10 betweenness centrality: {top_bet_cen}")
    print(f"Top 10 closeness centrality: {top_clo_cen}")
    print(f"Top 10 eigenvector centrality: {top_eig_cen}")
    print(f"Top 10 pagerank centrality: {top_pagerank_cen}")
    print(f"Reciprocity of the graph: {reciprocity_cen}")
    print(f"Diameter of the largest connected component: {nx.diameter(g)}")
    print(f"Correlation coefficient: {nx.transitivity(g)}")