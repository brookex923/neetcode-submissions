class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #need bfs with distances

        rows = len(grid)
        cols = len(grid[0])

        
        
        neighbors = [[0,1], [1,0], [-1,0], [0,-1]]

        def bfs(i, j):
            queue = deque()
            visited = set()
            queue.append([i, j, 0])
            visited.add((i,j))

            while queue:
                x, y, dist = queue.popleft()
                for dx, dy in neighbors:
                    newx = x + dx
                    newy = y + dy
                    if (newx < 0 or newy <0 or newx >= rows or newy >= cols or grid[newx][newy] == -1 or 
                    (newx, newy) in visited):
                        continue
                    
                    if grid[newx][newy] == 0:
                        visited.clear()
                        return dist + 1
                    else:
                        queue.append([newx, newy, dist+1])
                        visited.add((newx,newy))
            visited.clear()
            return 2147483647




        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)