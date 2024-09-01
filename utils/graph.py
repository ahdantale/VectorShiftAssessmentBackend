from collections import defaultdict
from collections import deque


def is_graph_dag(nodes,edges) :

    adjacency_list = defaultdict(list)
    indegree = defaultdict(int)

    queue = deque()
    topological_order = list()

    for node in nodes :
        adjacency_list[node["id"]] = list()

    for edge in edges : 
        adjacency_list[edge["source"]].append(edge["target"])

    for node in nodes : 
        indegree[node["id"]] = 0

    for node in nodes : 
        for neighbour in adjacency_list[node["id"]] :
            indegree[neighbour] += 1


    for node in indegree : 
        if indegree[node] == 0:
            queue.append(node)
            
    while queue :
        required_node = queue.popleft()
        topological_order.append(required_node)
        for neighbour in adjacency_list[required_node] :
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    print("TO",topological_order)
    
    return len(topological_order) == len(nodes)



