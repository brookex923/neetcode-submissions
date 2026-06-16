class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.hashmap:
            return res
        n = len(self.hashmap[key])
        l = 0
        r = n -1

        while l <= r:
            m = l + (r-l)//2
            if self.hashmap[key][m][1] <= timestamp:
                res = self.hashmap[key][m][0]
                l = m + 1 
            else:
                r = m - 1
        
        return res

        
