class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        length = len(unique)
        nums[:len(unique)] = unique
        return len(unique)