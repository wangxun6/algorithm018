class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        seen = set()
        seen.add(1)
        factors = [2, 3, 5]

        for _ in range(n):
            cur_ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = cur_ugly*f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return cur_ugly
