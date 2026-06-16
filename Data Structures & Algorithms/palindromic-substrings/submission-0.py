class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        grid = [[False] * n for i in range(n)]

        for i in range(n, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i<=2 or grid[i+1][j-1]):
                    grid[i][j] = True
                    count += 1
        
        return count
        