class Solution:
    def climbStairs(self, n: int) -> int:
        # at n - 1, there's 1 way
        # at n - 2, there's 1 + [n-1]
        # at n - 3, there's [n-1] + [n-2] ways 
        if n <= 2:
            return n

        steps = [0] * n

        steps[0] = 1
        steps[1] = 2

        i = 2
        while i < n:
            steps[i] = steps[i-1] + steps[i-2]
            i += 1
        
        return steps[n-1]
        