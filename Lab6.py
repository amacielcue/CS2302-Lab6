def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    # print edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
    if find(vertice1) != find(vertice2):
        union(vertice1, vertice2)
        minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)
#????


def kruskal():
    T = {}
    E =
    i = 1
    for i in range(E):
        if

def topologicsal(graph):
    all_in_degrees = compute_indegree_every_vertex(graph)
    sort_result = []
    q = Queue()
    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0
            q.put()
    while not q.is_empty():
        u = q.put()
        sort_result.append(u)
        for adj_vertex in graph.get_adj_vertices(u):
            all_in_degrees[adj_vertex] -= 1
            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)
    if len(sort_result) != graph.num_vertices:
        return None
    return sort_result
