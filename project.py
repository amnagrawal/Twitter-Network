import os
import twitter
from graph_utils import buildDirectedGraph, loadGraph
from network_measures import degree_distribution, draw_graph, centrality_measures

api = twitter.Api('''pleaase provide api keys''')

api.sleep_on_rate_limit = True

saved_graph_file = "./twitter_directed_graph"

dg = None
if os.path.isfile(saved_graph_file):
    # load the pre-saved graph if it already exists
    dg = loadGraph(saved_graph_file)

else:
    # Get the names of the users to query for
    with open('./names.csv', 'r') as f:
        queries = f.read().split('\n')[:-1]

    # Build a directed graph of the users' twitter network
    dg = buildDirectedGraph(api, queries)


degree_distribution(dg, title="Degree distribution of Directed Graph")
draw_graph(dg, "Directed graph")
print("For the directed graph, the centrality measures are:")
centrality_measures(dg)

ug = dg.to_undirected()
draw_graph(ug, "Undirected graph")
degree_distribution(ug, title="Degree distribution of Undirected Graph")
print("For the undirected graph, the centrality measures are:")
centrality_measures(ug)
