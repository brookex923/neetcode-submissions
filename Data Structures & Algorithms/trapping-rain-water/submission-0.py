class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        area = 0
        maxleft = [height[0]] * len(height)
        maxright = [height[-1]] * len(height)
        maxsofar = 0
        maxr=0

        for i in range(1, len(height)):
            maxsofar = max(maxsofar, height[i-1]) 
            maxleft[i] = maxsofar
        print(maxleft)
        for i in range(len(height)-2, -1, -1):
            maxr = max(maxr, height[i+1]) 
            maxright[i] = maxr
        print(maxright)
        
        for i in range(len(height)):
            curr = min(maxleft[i], maxright[i]) - height[i]
            print(curr)
            if curr >= 0:
                area += curr
        
        return area
