def populate_graph(graph, verticies, edges):
    for edge in range(edges):
        v1, v2, weight = map(int, input().split())
        graph.append((v1, v2, weight))

    return graph

def bellmanFord(src, graph):
    distDict = {k: float("Inf") for k in range(1, verticies + 1)}
    distDict[src] = 0

    for i in range(len(graph) - 1):
        for v1, v2, weight in graph:
            if distDict[v1] != float("Inf") and distDict[v1] + weight < distDict[v2]:
                distDict[v2] = distDict[v1] + weight

    for i in range(len(graph) - 1):
        for v1, v2, weight in graph:
            if distDict[v1] != float("Inf") and distDict[v1] + weight < distDict[v2]:
                return 1
    return -1





tests = int(input())
for i in range(tests):
    input()
    verticies, edges = map(int, input().split())
    graph = []
    graph = populate_graph(graph, verticies, edges)
    answerDict = bellmanFord(1,graph)
    print(answerDict)
