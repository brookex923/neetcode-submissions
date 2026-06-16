class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         
        small = 1
        large = max(piles)

        while small <= large:
            k = (small + large) // 2
            hours = 0
            for x in piles:
                hours += math.ceil(x/k)
            if hours > h:
                small = k+1
            elif hours <= h: 
                res = k #loop will keep going but will update correctly
                large = k-1
        
        return res
        

            




