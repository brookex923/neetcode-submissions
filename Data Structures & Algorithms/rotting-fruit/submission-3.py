class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        finallevel = 0
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(0,1), (1, 0), (0,-1), (-1,0)]
        rotten = deque()

    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j, 0))
        
        ran = False
        while rotten:
            ran = True
            x, y, level = rotten.popleft()
            for dx, dy in neighbors:
                newx = x + dx
                newy = y + dy
                if 0<=newx<rows and 0<=newy<cols:
                    if grid[newx][newy] == 1:
                        rotten.append((newx, newy, level+1))
                        grid[newx][newy] = 2
        if ran:
            finallevel = level
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return finallevel
        