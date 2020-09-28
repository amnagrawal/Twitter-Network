import pickle

import networkx as nx


def getUserFromName(name, api):
    user_list = api.GetUsersSearch(term=name, page=1, count=1)
    if user_list:
        user = user_list[0]
        if user.verified and (not user.protected):
            return user
    return None


def loadGraph(file="./twitter_directed_graph"):
    with open(file, 'rb') as f:
        graph = pickle.load(f)

    print(len(graph.nodes))
    count = 0
    to_remove = []
    for i, node in enumerate(graph.nodes):
        if graph.degree(node) < 15 or graph.degree(node) > 110:
            count += 1
            to_remove.append(node)

    for node in to_remove:
        graph.remove_node(node)

    print(count)
    print(graph.nodes)
    return graph


def buildDirectedGraph(api, queries):
    dg = nx.DiGraph()
    id_to_name = {}

    # Add nodes to the graph
    for i in range(len(queries)):
        user = getUserFromName(queries[i], api)

        if user:
            id_to_name[user.id] = user.name
            dg.add_node(user.name, id=repr(user.id), screen_name=user.screen_name)
            queries[i] = user.name

    # Add edges to the graph
    for query_name in queries:

        if not dg.has_node(query_name):
            print(f"Skipping {query_name}")
            continue

        query_id = dg.nodes[query_name]['id']
        friendIDs = api.GetFriendIDs(query_id)

        # This takes time as access to the API is rate limited
        for friendID in friendIDs:
            if friendID in id_to_name.keys():

                friend_name = id_to_name[friendID]
                # print(f'{query_name} is following {friend_name}')
                dg.add_edge(query_name, friend_name)

    return dg