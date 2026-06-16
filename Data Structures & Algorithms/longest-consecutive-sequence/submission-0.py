class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        streak = 1
        maxstreak = 1

        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i+1] == nums[i] +1:
                streak+= 1
            else:
                maxstreak = max(maxstreak, streak)
                streak = 1
        maxstreak = max(maxstreak, streak)
        return maxstreak





