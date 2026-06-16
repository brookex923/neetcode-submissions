class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min cost of current floor is min (totcost[i-1] + cost[i-1], totcost[i-2] + cost[i-2])

        totcost = [-1] * (len(cost)+1)
        n = len(cost)

        totcost[0] = 0
        totcost[1] = 0

        #dp i represents min cost to get to ith stair
        for i in range(2, n+1):
            totcost[i] = min(totcost[i-1] + cost[i-1], totcost[i-2] + cost[i-2])
            

        return totcost[n]