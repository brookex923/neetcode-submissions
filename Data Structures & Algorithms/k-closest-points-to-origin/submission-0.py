class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # maintain a minheap of length k
        distances = []
        hashmap = {}
        res = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            distances.append(distance * -1)
            hashmap[distance] = hashmap.get(distance, []) + [point]
        
        heapq.heapify(distances)

        while len(distances) > k:
            heapq.heappop(distances)
        
        for d in distances:
            for p in hashmap[d*-1]:
                if len(res) >= k:
                    break
                res.append(p)
        
        return res


        