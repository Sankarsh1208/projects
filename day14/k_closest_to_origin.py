from collections import defaultdict

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        ans = []
        heap = []
        for x, y in points:
            d = x*x + y*y
            heap.append((d, x, y))
        heapq.heapify(heap)
        for _ in range(k):
            val = heapq.heappop(heap)
            ans.append([val[1], val[2]])
        return ans