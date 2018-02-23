
current_edge = 0
initial_input = input()

verticies, edges = initial_input.split()
verticies = int(verticies)
edges = int(edges)

graph = set(range(1, verticies + 1))
graph = dict.fromkeys(graph, 0)

while current_edge < edges:
    string = input()
    v1,v2 = string.split()
    v1 = int(v1)
    v2 = int(v2)
    graph[v1] += 1
    graph[v2] += 1

    current_edge += 1

for vertex in graph.keys():
    print(graph[vertex])


