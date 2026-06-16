class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        # let cache[i] store the number of ways to get to step 1 given that
        # we are at step i
        
        def dp(i):
            if i == n:
                return 1
            if i > n:
                return 0

            if cache[i] != -1:
                # not yet visited
                return cache[i]
            cache[i] = dp(i+1) + dp(i+2)
            return cache[i]
        
        return dp(0)
        