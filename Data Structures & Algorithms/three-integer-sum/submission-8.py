class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        answer = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i!=0 and nums[i-1] == nums[i]: #skip over i dupes
                continue
            l = i+1
            r = len(nums) - 1
            while l<r:
                if nums[l] + nums[r] > -nums[i]: #too big
                    r-=1
                elif nums[l] + nums [r] < -nums[i]: #too small
                    l += 1
                     
                else:
                    answer.append([nums[l], nums[r], nums[i]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        
        return answer
        