def bfs(graph, node):
    visited = set()
    visited.add(node)
    q = [node]

    while q:
        node = q.pop(0)
        print(node, end=" ")

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

graph = {
    'A': ['B', 'C'],'B': ['A', 'D'],'C': ['A', 'D'],'D': ['C', 'B', 'E'],'E': []
}
bfs(graph, 'A')