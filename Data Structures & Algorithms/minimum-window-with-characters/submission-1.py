class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        for letter in t:
            freq_t[letter] = 1 + freq_t.get(letter, 0)
        
        have = 0
        need = len(freq_t)
        res = [-1, -1]
        min_length = float('inf')

        left = 0

        for right in range(len(s)):
            curr_letter = s[right]
            freq_s[curr_letter] = 1 + freq_s.get(curr_letter, 0)
            if curr_letter in freq_t and freq_s[curr_letter] == freq_t[curr_letter]:
                have += 1
            
            while have == need:
                if right - left + 1 <min_length:
                    res = [left, right+1]
                    min_length = right-left+1
                
                letter_cut = s[left]
                left += 1
                freq_s[letter_cut] -= 1
                if letter_cut in freq_t and freq_s[letter_cut] < freq_t[letter_cut]:
                    have -= 1
        if min_length == float('inf'):
            return ""

        l = res[0]
        r = res[1]
        
        return s[l:r]



        