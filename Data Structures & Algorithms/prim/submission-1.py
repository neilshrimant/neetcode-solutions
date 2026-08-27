class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n+1):
            adj[i] = []
        
        for src, dst, w in edges:
            adj[src].append([dst,w])
            adj[dst].append([src,w])
        
        minHeap = []

        for neighbor, w in adj[1]:
            heapq.heappush(minHeap, [w, 1, neighbor])
        total = 0
        visit = set()
        visit.add(1)

        while minHeap:
            w, src, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            total += w
            visit.add(node)
            for neighbor, weight in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, node, neighbor])
        
        return total if len(visit) == n else -1