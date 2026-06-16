class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        freq = defaultdict(int)
        key = defaultdict(int)
        for c in s1:
            key[c] +=1 
        l = 0
        r = 0

        for r in range(len(s2)):
            freq[s2[r]] += 1
            if r-l+1 == len(s1):
                if Counter(freq) == Counter(key):
                    return True
                else:
                    freq[s2[l]] -=1 
                    if freq[s2[l]] == 0:
                        del freq[s2[l]]
                    print(freq)
                    l+=1
            
                
        
        return False
