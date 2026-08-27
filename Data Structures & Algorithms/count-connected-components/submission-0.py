class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * (n)
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p1] += self.rank[p2]

        return True
         


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
       dsu = UnionFind(n)
       for a, b in edges:
        dsu.union(a,b)
       return len(set(dsu.find(x) for x in range(n)))
         

        