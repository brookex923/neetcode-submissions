class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min cost of current floor is min (totcost[i-1] + cost[i-1], totcost[i-2] + cost[i-2])

        totcost = [-1] * (len(cost)+1)
        n = len(cost)

        totcost[0] = 0
        totcost[1] = 0

        #dp i represents min cost to get to ith stair
        def dp(i):
            if totcost[i] != -1:
                return totcost[i]
            
            totcost[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            return totcost[i]

        return dp(n)