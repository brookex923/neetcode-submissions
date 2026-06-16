class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        neighbors = [[0,1], [1, 0], [-1, 0], [0, -1]]

        def dfs(i, j):
            if (i<0 or j<0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"
            for x, y in neighbors:
                dfs(i+x, j+y)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        
        return res

        

            
        