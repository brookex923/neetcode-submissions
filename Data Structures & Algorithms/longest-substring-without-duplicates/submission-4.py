class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlength = 1
        length=1
        l,r = 0,0
        seen = set()

        while r<len(s):
            print(seen)
            if s[r] not in seen:
                seen.add(s[r])
                
                maxlength = max(len(seen), maxlength)
                r+=1
            else: #s[r] in seen
                seen.clear()
                l+=1
                r = l
                
                
        return maxlength