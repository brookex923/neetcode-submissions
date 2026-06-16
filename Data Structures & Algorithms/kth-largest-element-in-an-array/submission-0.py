class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain max heap with k largest
        maxHeap = [-s for s in nums]
        heapq.heapify(maxHeap)

        while len(maxHeap) > len(nums) - k:
            ans = heapq.heappop(maxHeap)
        
        return ans * -1
        