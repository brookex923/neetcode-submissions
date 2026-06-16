class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        longest = ""
        for i in range(n, -1, -1):
            for j in range(i, n):
                if i+1>= n or j<=0 : 
                    prev=0
                else :
                    prev = dp[i+1][j-1]
                if j - i <= 2 and s[i] == s[j]:
                    dp[i][j] = j - i + 1
                elif s[i] == s[j] and prev != 0:
                    dp[i][j] = prev + 2
                
                if dp[i][j] > len(longest):
                    longest = s[i:j+1]
        
        return longest
                

                     


        