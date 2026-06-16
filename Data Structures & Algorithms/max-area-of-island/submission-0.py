class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [[0,1], [1,0], [-1,0], [0,-1]]

        def dfs(i, j):
            if i <0 or j < 0 or i>=rows or j>=cols or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return (1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1))
        
        area = 0
        for i in range(rows):
            for j in range(cols):
                area = max(area, dfs(i,j))
        
        return area

            


        