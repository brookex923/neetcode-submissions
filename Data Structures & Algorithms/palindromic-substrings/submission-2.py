class Solution:
    def countSubstrings(self, s: str) -> int:
        ''' counter = 0
        for center in range(len(s)):
            left = center
            right = center
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    counter += 1
                    left -= 1
                    right += 1
        
        '''
        hashmap = {}


        def check_p(s, left, right) : 
            while right >= left :
                if s[right] != s[left] : 
                    return False 
                right-=1
                left +=1
            return True

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], []) + [i]
        count =0
        for ch in hashmap.keys():
            indexes = hashmap[ch]

            for i in range(len(indexes)) :
                count +=1
                for j in range(i+1, len(indexes)) : 
                    if check_p (s, indexes[i], indexes[j]) : 
                        count +=1

        return count


        



        