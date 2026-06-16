class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        
        front = []
        back = nums
        
        while len(back) >0:
            product = 1
            for f in front:
                product *= f
            current = back.pop(0)
            for b in back:
                product *= b
            front.append(current)
            answer.append(product)
        return answer
         