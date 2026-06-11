def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for nei in graph[node]:
        if nei not in visited:
            dfs(graph, nei, visited)

graph = {
    'A': ['B', 'C'],'B': ['A', 'D'],'C': ['A', 'D'],'D': ['C', 'B', 'E'],'E': []
}

dfs(graph, 'A')