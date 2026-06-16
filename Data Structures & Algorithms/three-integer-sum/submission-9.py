class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        x = 0
        while x < len(nums):
            if nums[x] > 0:
                break # no more pairs
            l = x + 1
            r = len(nums) - 1 
            target = nums[x] * -1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ans.append([nums[x], nums[l], nums[r]])
                    while l < len(nums) - 2 and nums[l+1] == nums[l]:
                        l += 1
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
                    r -= 1
                    l += 1
            
            # skip duplicates
            while x < len(nums) - 2 and nums[x+1] == nums[x]:
                x += 1
            x += 1 
        
        return ans



            
            