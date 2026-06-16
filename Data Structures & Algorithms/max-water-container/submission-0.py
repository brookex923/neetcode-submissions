class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        answer = 0
        #print(str(l) + "and" + str(r))
        
        
        while l<r:
            width = r-l
            height = min(heights[l], heights[r])
            area = width*height
            answer = max(answer, area)
            if heights[l] < heights[r]: #if left is short
                l+=1 
            elif heights[l] >= heights[r]: #if right is short
                r-=1
            #print(str(answer) + " left: " + str(l) + "right: " + str(r))
        answer = max(answer, area)
        return answer
    
