class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        
        l, r = 0, len(height) -1
        area = 0
        maxL = height[0]
        maxR = height[-1]

        while l < r:
            if maxL <= maxR:
                l+=1
                maxL = max(maxL, height[l])
                area += maxL - height[l]
            elif maxR < maxL:
                r -= 1
                maxR = max(maxR, height[r])
                area += maxR - height[r]

        return area
