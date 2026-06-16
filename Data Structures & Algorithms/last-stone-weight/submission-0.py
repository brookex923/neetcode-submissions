class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-s for s in stones]
        heapq.heapify(stone_heap)
        
        while len(stone_heap) > 1:
            x = heapq.heappop(stone_heap)
            y = heapq.heappop(stone_heap)

            if x < y:
                heapq.heappush(stone_heap, x-y)
        
        if len(stone_heap) == 1:
            return abs(heapq.heappop(stone_heap))
        else:
            return 0

