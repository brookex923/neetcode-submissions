class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        sol = []

        def backtrack(i, sol, sum):

            if sum == target:
                result.append(sol[:])
                return
            
            if sum > target or i >= len(nums):
                return 
            # add
            sol.append(nums[i])
            backtrack(i, sol, sum + nums[i])
            sol.pop()
            # don't add
            backtrack(i + 1, sol, sum)
        
        backtrack(0, [], 0)
        return result
