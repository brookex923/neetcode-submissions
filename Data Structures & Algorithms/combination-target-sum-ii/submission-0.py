class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sol = []
        
        candidates.sort()

        def backtrack(i, sol, sum):
            if sum == target:
                result.append(sol[:])
                return
            
            if sum > target or i >= len(candidates):
                return
            
            sol.append(candidates[i])
            backtrack(i+1, sol, sum + candidates[i])
            sol.pop()

            # don't add
            while i+1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i+1, sol, sum)

        backtrack(0, [], 0)
        return result



