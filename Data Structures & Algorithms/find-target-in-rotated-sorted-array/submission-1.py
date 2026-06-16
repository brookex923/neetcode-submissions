class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        rotated = (6-nums[0]) + 1
        while l<r:
            #find pivot
            while l < r:
                m = (l+r)//2
                if nums[m] > nums[r]:
                    l = m+1
                elif nums[m] < nums[r]:
                    r = m

        pivot = l  

        def binary_search(l: int, r: int) -> int:
            while l<=r:
                m = (l+r)//2
                if target < nums[m]:
                    r = m-1
                elif target > nums[m]:
                    l = m+1
                elif target == nums[m]:
                    return m
            return -1
        
        result = binary_search(0, pivot-1)
        if result == -1:
            return binary_search(pivot, len(nums)-1)
        else:
            return result
            
                          


                
        
        return -1


            