class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for index1 in range(len(numbers)):
            diff = target - numbers[index1]
            if diff in numbers and numbers.index(diff) > index1:
                return [index1+1, numbers.index(diff)+1]