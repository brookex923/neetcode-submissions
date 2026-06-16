class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for center in range(len(s)):
            #odd length
            left, right = center, center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1
            
            #even length
            left, right = center, center+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1
        
        return longest

        