class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dict where the value to each key is how frequent an int appears
        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num] += 1
        
        sorted_items_list = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
        print(sorted_items_list)
        answer = []
        i = 0
        while i < k:
            get = sorted_items_list[i][0]
            answer.append(get)
            i+=1
        return answer

        