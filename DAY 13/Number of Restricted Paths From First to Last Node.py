# There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

# A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

# The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

# Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.
import heapq
from functools import lru_cache

class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        graph = [[] for _ in range(n + 1)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra from node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0

        pq = [(0, n)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nei, w in graph[node]:
                nd = d + w

                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(pq, (nd, nei))

        @lru_cache(None)
        def dfs(node):
            if node == n:
                return 1

            paths = 0

            for nei, _ in graph[node]:
                if dist[nei] < dist[node]:
                    paths = (paths + dfs(nei)) % MOD

            return paths

        return dfs(1)