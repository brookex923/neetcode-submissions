class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 1
        curr_length = 1

        if not nums:
            return 0
            
        seen = set()

        for n in nums:
            seen.add(n)
        
        for n in nums:
            if n-1 not in seen:
                while n + curr_length in seen:
                    curr_length += 1
                    max_length = max(max_length, curr_length)
                
                curr_length = 1



          
        
        return max_length
            


        