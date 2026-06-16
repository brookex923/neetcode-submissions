class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        curr_prefix = 1
        curr_postfix = 1

        for i in range(len(nums)):
            curr_prefix *= nums[i]
            prefix[i] = curr_prefix

        for i in range(len(nums)-1, 0, -1):
            curr_postfix *= nums[i]
            postfix[i] = curr_postfix

        for i in range(len(nums)):
            if i == 0:
                answer[i] = postfix[i+1]
            elif i == len(nums) - 1:
                answer[i] = prefix[i-1]
            else:
                answer[i] = prefix[i-1] * postfix[i+1]
        
        return answer
            

        
        
         