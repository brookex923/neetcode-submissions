class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two pass hashmap
        seen = {}
        for i, num in enumerate(nums):
            seen[num] = i #map value to index
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen and seen[diff] != i:
                return [i, seen[diff]]
        


            