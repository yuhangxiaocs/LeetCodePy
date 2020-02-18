from collections import deque


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = {}

        for a, b in edges:
            if a in adj:
                adj[a].append(b)
            else:
                adj[a] = [b]

            if b in adj:
                adj[b].append(a)
            else:
                adj[b] = [a]

        res = [0] * N

        for i in range(N):
            vis = [0] * N
            vis[i] = 1
            q = deque()
            q.extend(adj[i][:])

            level = 0

            while q:
                x = len(q)
                level += 1

                while x:
                    x -= 1
                    node = q.popleft()
                    if vis[node] == 0:
                        vis[node] = 1
                        res[i] += level
                        q.extend(adj[node])

        return res


if __name__ == '__main__':
    obj = Solution()

    N = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(obj.sumOfDistancesInTree(N, edges))
