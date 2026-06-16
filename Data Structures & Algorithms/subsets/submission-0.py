class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            curr = []
            for item in result:
                curr.append(item + [num])
            result.extend(curr)    
        
        return result
        