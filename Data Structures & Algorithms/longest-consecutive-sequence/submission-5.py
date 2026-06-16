class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        streak = []
        streaklength = 1
        maxstreak = 1
        i=0
        while i < len(nums) and streaklength<= len(nums):
            if nums[i] + streaklength in nums:
                streaklength += 1
                maxstreak = max(maxstreak, streaklength)
            else: 
                i+=1
                streaklength = 1
        maxstreak = max(maxstreak, streaklength)
        return maxstreak


        





