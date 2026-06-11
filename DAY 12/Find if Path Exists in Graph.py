#( 1971 )There is a bi-directional graph with n vertices,
#where each vertex is labeled from 0 to n - 1 (inclusive).
#The edges in the graph are represented as a 2D integer array edges,
#where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
# Every vertex pair is connected by at most one edge, 
#and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists
 #from vertex source to vertex destination.
# Given edges and the integers n, source, and destination,
# return true if there is a valid path from source to destination, or false otherwise.

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True

            return False

        return dfs(source)