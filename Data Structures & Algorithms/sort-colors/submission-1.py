class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        numZeros = hashmap.get(0, 0)
        numOnes = hashmap.get(1, 0)
        numTwos = hashmap.get(2, 0)

        for i in range(numZeros):
            nums[i] = 0
        
        for i in range(numZeros, numZeros + numOnes):
            nums[i] = 1
        
        for i in range(numZeros + numOnes, len(nums)):
            nums[i] = 2
        
        
