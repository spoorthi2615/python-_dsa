# #There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
#and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and
#no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
# and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()

        def dfs(city):
            visited.add(city)

            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in visited:
                    dfs(nei)

        provinces = 0

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces
 