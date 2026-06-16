class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket approach
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
            # count[num] = 1 + count.get(num, 0)
        for number, freqs in count.items():
            freq[freqs].append(number)

        answer = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                answer.append(num)
            if len(answer) == k:
                return answer


        