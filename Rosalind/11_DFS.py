def dfs(graph, visited, v):
    visited[v] = True
    for adj in graph[v]:
        if not visited[adj]:
            dfs(graph, visited, adj)

def find_components(graph):
    connected_sum = 0
    visited = [None] * len(graph)
    for i in range(len(visited)):
        if not visited[i]:
            connected_sum += 1
            dfs(graph, visited, i)
    return connected_sum

def main():
    verticies, edges = map(int, input().split())
    graph = [[] for i in range(verticies)]
    for i in range(edges):
        v1, v2 = map(int, input().split())
        graph[v1 - 1].append(v2 - 1)
        graph[v2 - 1].append(v1 - 1)
    print(find_components(graph))

main()
