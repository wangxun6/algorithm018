class UF:
    parent = {}
    cnt = 0

    def __init__(self, M):
        n = len(M)
        for i in range(n):
            self.parent[i] = i
            self.cnt += 1

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q): return
        self.parent[self.find(p)] = self.find(q)
        self.cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UF(M)
        for i in range(n):
            for j in range(i):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.cnt
